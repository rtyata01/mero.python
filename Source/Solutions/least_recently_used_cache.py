from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
    
    def put(self, key: int, value: int):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last = False)
        self.cache[key] = value
        
cache = LRUCache(capacity=3)
cache.put(1,11)
cache.put(2,22)
cache.put(3,33)
cache.put(3,3333)
print(f"Get cache: {cache.get(1)}")
print(f"Get cache: {cache.get(3)}")
cache.put(4,44)
cache.put(4,444)
print(f"Get cache: {cache.get(2)}") # returns -1, since key was removed due to capacity limit.
print(f"Get cache: {cache.get(4)}")
