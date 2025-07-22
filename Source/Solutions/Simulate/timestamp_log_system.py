# You are given a log system where each log has a unique ID and a timestamp (format: "YYYY:MM:DD:HH:MM:SS"). Implement two methods:
# put(id: int, timestamp: str) -> None
# retrieve(start: str, end: str, granularity: str) -> List[int]

from typing import List

class LogSystem:
    def __init__(self):
        # Store logs as list of (id, timestamp) tuples
        self.logs = []
        # Map granularity to timestamp truncation length
        self.granularity_map = {
            "Year": 4,    # YYYY
            "Month": 7,   # YYYY:MM
            "Day": 10,    # YYYY:MM:DD
            "Hour": 13,   # YYYY:MM:DD:HH
            "Minute": 16, # YYYY:MM:DD:HH:MM
            "Second": 19  # YYYY:MM:DD:HH:MM:SS
        }

    def put(self, id: int, timestamp: str) -> None:
        # Append log with id and timestamp
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        # Convert granularity to title case for case-insensitive matching
        granularity = granularity.title()
        # Get truncation length for granularity
        trunc_len = self.granularity_map[granularity]
        # Truncate start and end timestamps
        start_trunc = start[:trunc_len]
        end_trunc = end[:trunc_len]
        # Return IDs where truncated timestamp is in range
        return [id for id, ts in self.logs if start_trunc <= ts[:trunc_len] <= end_trunc]
    
log = LogSystem()
log.put(1, "2023:01:02:12:00:00")
log.put(2, "2023:01:02:12:00:00")
log.put(3, "2023:02:02:12:00:00")
log.put(4, "2023:03:02:12:00:00")
# Retrieve request IDs for January 2023
request_ids = log.retrieve("2023:01:01:00:00:00", "2023:01:31:23:59:59", "Month")
print (f"Result: ", request_ids)
request_ids = log.retrieve("2023:01:01:00:00:00", "2023:12:31:23:59:59", "mOnth")
print (f"Result: ", request_ids)