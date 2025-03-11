from rate_limiter_timer import RateLimiter
import time

class ApiController:
    def __init__(self) -> None:
        self.rate_limit_config = {}
        
    def get_rate_limiter(self, user_id: str) -> RateLimiter:
        if user_id not in self.rate_limit_config:
            self.rate_limit_config[user_id] = RateLimiter(n=3, t=2)
        
        return self.rate_limit_config[user_id]
    
    def handle_user_requests(self, user_id: str) -> str:
        rate_limiter = self.rate_limit_config(user_id)
        
        if rate_limiter.allow():
            return "Request Allowed"
        else:
            return "Rate Limit Exceeded!"


api = ApiController()
user_first = "user1"
user_second = "user2"

for i in range(5):
    print(f"Requests [{i}] for user [{user_first}]", api.handle_user_requests(user_first))
    print(f"Requests [{i}] for user [{user_second}]", api.handle_user_requests(user_second))

