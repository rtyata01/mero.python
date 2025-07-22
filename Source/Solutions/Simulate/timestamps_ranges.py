# Problem:Given a sorted list of timestamps (in seconds), and a new timestamp t, find all timestamps within ±k seconds of t.

from typing import List
from bisect import bisect_left, bisect_right

def find_timestamps(timestamps: List[int], t: int, k: int) -> List[int]:
    # Find the range [t - k, t + k] using binary search
    left = bisect_left(timestamps, t - k)
    right = bisect_right(timestamps, t + k)
    # Return timestamps in the range
    return timestamps[left:right]

print(f"Timetamp ranges: ", find_timestamps([100, 125, 150, 200, 250, 300], t=200, k=50))
print(f"Timetamp ranges: ", find_timestamps([100, 125, 150, 200, 250, 300], t=200, k=75))
print(f"Timetamp ranges: ", find_timestamps([100, 125, 150, 200, 250, 300], t=200, k=100))