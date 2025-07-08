from collections import deque
import time

class RateLimiter:
    def __init__(self, n: int, t: int):  # improvments - add redis_client cache, user_id: str,
        self.n = n
        self.t = t
        self.queue = deque()
        
    def allow(self) -> bool:
        current_time = time.time()
        
        while self.queue and self.queue[0] < current_time - self.t:
            self.queue.popleft()
            print(f"Dequeuing requests: {current_time - self.t}")
        
        if len(self.queue) < self.n:
            print(f"Queuing requests: {current_time}")
            self.queue.append(current_time)
            return True
        else:
            return False    

# Let's simulate this with n=3 requests per t=5 seconds.    
limiter = RateLimiter(n=3, t=5)

for i in range(5):
    print(f"Request {i+1}: {'Allowed' if limiter.allow() else 'Blocked'}")
    time.sleep(1)  # Wait 1 second between requests