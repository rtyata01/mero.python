import httpx
import json
from datetime import datetime

# API base URL (update if deployed to cloud, e.g., https://your-app.onrender.com)
BASE_URL = "http://localhost:8000"

async def fetch_and_store_stock_data(ticker: str, start_date: str, end_date: str):
    """
    Call POST /api/stock_data to fetch and store historical stock data.
    """
    url = f"{BASE_URL}/api/stock_data"
    payload = {
        "ticker": ticker,
        "start_date": start_date,
        "end_date": end_date
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=payload)
            response.raise_for_status()  # Raises exception for 4xx/5xx errors
            data = response.json()
            print(f"\nFetched and stored data for {ticker}:")
            print(json.dumps(data, indent=2))
            return data
        except httpx.HTTPStatusError as e:
            print(f"Error fetching data: {e.response.status_code} - {e.response.text}")
        except httpx.RequestError as e:
            print(f"Network error: {str(e)}")

async def get_stored_stock_data(ticker: str, start_date: str, end_date: str):
    """
    Call GET /api/stock_data/{ticker} to retrieve stored stock data.
    """
    url = f"{BASE_URL}/api/stock_data/{ticker}?start_date={start_date}&end_date={end_date}"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            print(f"\nRetrieved stored data for {ticker}:")
            print(json.dumps(data, indent=2))
            return data
        except httpx.HTTPStatusError as e:
            print(f"Error retrieving data: {e.response.status_code} - {e.response.text}")
        except httpx.RequestError as e:
            print(f"Network error: {str(e)}")

async def main():
    """
    Example usage of the client to call the API.
    """
    ticker = "TSLA"
    start_date = "2025-01-01"
    end_date = "2025-07-07"

    # Fetch and store stock data
    await fetch_and_store_stock_data(ticker, start_date, end_date)

    # Retrieve stored stock data
    await get_stored_stock_data(ticker, start_date, end_date)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())