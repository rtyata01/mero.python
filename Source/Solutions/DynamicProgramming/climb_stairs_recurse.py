class Solution:
    def recurse(self, n, cache=None):
        if cache is None:
            cache = {}
            
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        if n in cache:
            return cache[n]
        
        cache[n] = self.num_stairs(n-1) + self.num_stairs(n-2)
        return cache[n]
    
    def num_stairs(self, n):
        return self.recurse(n)
    
sln = Solution()
result = sln.num_stairs(5)
print(f"Number of ways:", result)