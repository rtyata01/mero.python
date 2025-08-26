# Initialize Bucket: Set the bucket size and the rate at which tokens are generated.
# Token Generation: Add tokens at a fixed rate to the bucket.
# Request Handling: When a request comes, check if there's a token available in the bucket. 
# If yes, allow the request and consume a token; if no, deny or delay the request.

import time
import threading

class TokenBucket:
    def __init__(self, rate, capacity):
        """
        Initialize the TokenBucket.
        rate: Number of tokens added to the bucket per second.
        capacity: Maximum number of tokens the bucket can hold.
        """
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.last_checked = time.time()
        self.lock = threading.Lock()
    
    def add_tokens(self):
        """
        Adds tokens to the bucket at the specified rate.
        """
        current_time = time.time()
        elapsed_time = current_time - self.last_checked
        
        # Add tokens at the rate of 1 token per second
        new_tokens = int(elapsed_time * self.rate)
        
        if new_tokens > 0:
            # Avoid overflowing the bucket
            self.tokens = min(self.capacity, self.tokens + new_tokens)
            self.last_checked = current_time

    def allow_request(self):
        """
        Check if a request can be allowed (if there's a token available).
        """
        with self.lock:
            self.add_tokens()
            
            if self.tokens > 0:
                self.tokens -= 1  # Consume one token
                return True  # Request allowed
            else:
                return False  # Request denied

def simulate_requests(token_bucket):
    for i in range(20):
        if token_bucket.allow_request():
            print(f"Request {i+1} allowed.")
        else:
            print(f"Request {i+1} denied.")
        time.sleep(0.2)  # Simulate time between requests

if __name__ == "__main__":
    # Initialize token bucket with a rate of 2 tokens per second and capacity of 5 tokens
    bucket = TokenBucket(rate=2, capacity=5)
    
    # Simulate some incoming requests
    simulate_requests(bucket)
