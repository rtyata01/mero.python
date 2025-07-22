# Design a class that supports calendar bookings without double booking:
# book(start: int, end: int) -> bool
# If a booking conflicts with a previous one (overlap), return False. Otherwise book and return True.

class CalendarBooking:
    def __init__(self):
        # Store bookings as list of (start, end) tuples
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        # Check for overlap with existing bookings
        for s, e in self.bookings:
            if start < e and end > s:
                return False
            
        # No overlap, add booking
        self.bookings.append((start, end))
        return True
    
calendar = CalendarBooking()
print(calendar.book(10, 20))  # True (book [10, 20))
print(calendar.book(15, 25))  # False (overlaps with [10, 20))
print(calendar.book(20, 30))  # True (no overlap, books [20, 30))
print(calendar.book(5, 15))   # False (overlaps with [10, 20))