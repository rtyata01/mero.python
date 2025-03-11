import unittest
import time
from rate_limiter_timer import RateLimiter

class TestRateLimiter(unittest.TestCase):
    def test_zero_requests(self):
        print("Running tests ....................")
        rate_limiter = RateLimiter(n=0, t=1)
        self.assertFalse(rate_limiter.allow())
        time.sleep(1)
        self.assertFalse(rate_limiter.allow())
        
    def test_zero_time_window(self):
        print("Running tests ....................")
        rate_limiter = RateLimiter(n=2, t=0)
        self.assertTrue(rate_limiter.allow())
        self.assertTrue(rate_limiter.allow())        
        self.assertFalse(rate_limiter.allow())
        time.sleep(1)
        self.assertTrue(rate_limiter.allow())
    
    def test_rate_limiting(self):
        print("Running tests ....................")
        rate_limiter = RateLimiter(n=2, t=1)
        self.assertTrue(rate_limiter.allow())
        self.assertTrue(rate_limiter.allow())        
        self.assertFalse(rate_limiter.allow())
        time.sleep(1)
        self.assertTrue(rate_limiter.allow())

if __name__ == "__main__":
    unittest.main()