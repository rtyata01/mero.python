from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import yfinance as yf
import sqlite3
from typing import List
import logging
from fastapi.responses import JSONResponse

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Historical Stock Data API")

# Pydantic models for request/response
class StockRequest(BaseModel):
    ticker: str
    start_date: str  # Format: YYYY-MM-DD
    end_date: str    # Format: YYYY-MM-DD

class StockDataResponse(BaseModel):
    date: str
    ticker: str
    open: float
    high: float
    low: float
    close: float
    volume: int

# POST: Fetch and store historical stock data
@app.post("/api/stock_data", response_model=List[StockDataResponse])
async def fetch_stock_data(request: StockRequest):
    try:
        # Validate date format
        start_date = datetime.strptime(request.start_date, "%Y-%m-%d")
        end_date = datetime.strptime(request.end_date, "%Y-%m-%d")
        if start_date >= end_date:
            raise HTTPException(status_code=400, detail="start_date must be before end_date")

        # Fetch data from yfinance
        stock = yf.Ticker(request.ticker)
        df = stock.history(start=request.start_date, end=request.end_date)

        if df.empty:
            raise HTTPException(status_code=404, detail=f"No data found for ticker {request.ticker}")

        # Store data in SQLite
        conn = sqlite3.connect("stock_data.db")
        cursor = conn.cursor()
        stock_data = []
        for date, row in df.iterrows():
            date_str = date.strftime("%Y-%m-%d")
            cursor.execute("""
                INSERT OR REPLACE INTO stock_data (ticker, date, open, high, low, close, volume)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                request.ticker,
                date_str,
                row["Open"],
                row["High"],
                row["Low"],
                row["Close"],
                int(row["Volume"])
            ))
            stock_data.append({
                "date": date_str,
                "ticker": request.ticker,
                "open": row["Open"],
                "high": row["High"],
                "low": row["Low"],
                "close": row["Close"],
                "volume": int(row["Volume"])
            })
        conn.commit()
        conn.close()

        logger.info(f"Stored {len(stock_data)} records for ticker {request.ticker}")
        return stock_data
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid date format: {str(e)}")
    except Exception as e:
        logger.error(f"Error fetching/storing data for {request.ticker}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# GET: Retrieve stored stock data by ticker and date range
@app.get("/api/stock_data/{ticker}", response_model=List[StockDataResponse])
async def get_stock_data(ticker: str, start_date: str = None, end_date: str = None):
    try:
        conn = sqlite3.connect("stock_data.db")
        cursor = conn.cursor()
        query = "SELECT date, ticker, open, high, low, close, volume FROM stock_data WHERE ticker = ?"
        params = [ticker]

        if start_date and end_date:
            try:
                datetime.strptime(start_date, "%Y-%m-%d")
                datetime.strptime(end_date, "%Y-%m-%d")
                query += " AND date >= ? AND date <= ?"
                params.extend([start_date, end_date])
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid date format")

        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            raise HTTPException(status_code=404, detail=f"No data found for ticker {ticker}")

        return [
            {
                "date": row[0],
                "ticker": row[1],
                "open": row[2],
                "high": row[3],
                "low": row[4],
                "close": row[5],
                "volume": row[6]
            }
            for row in rows
        ]
    except Exception as e:
        logger.error(f"Error retrieving data for {ticker}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")