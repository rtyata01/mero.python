# Design and implement a data structure for a Least Frequently Used (LFU) cache.
# Eviction criterion: Remove the item that has been accessed the fewest number of times.
# Tracks: Frequency of access.
# Cache entries that are rarely used are less valuable and should be evicted first, regardless of how recently they were accessed.

from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val_freq = {}  # key: (value, frequency)
        self.freq_to_keys = defaultdict(OrderedDict)  # OrderedDiction within default dictionary.
        self.min_freq = 0

    def _update_freq(self, key):
        val, freq = self.key_to_val_freq[key]
        # Remove from current frequency
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if freq == self.min_freq:
                self.min_freq += 1
        # Add to next frequency
        self.freq_to_keys[freq + 1][key] = None
        self.key_to_val_freq[key] = (val, freq + 1)

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        self._update_freq(key)
        return self.key_to_val_freq[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val_freq:
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
            self._update_freq(key)
            return

        if len(self.key_to_val_freq) >= self.capacity:
            # Evict the LRU key with min frequency
            key_to_evict, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[key_to_evict]
            if not self.freq_to_keys[self.min_freq]:
                del self.freq_to_keys[self.min_freq]

        # Insert new key
        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = None # use None as value.
        self.min_freq = 1

lfu = LFUCache(capacity=3)
lfu.put(1, 1)
lfu.put(2, 2)
lfu.put(3, 3)
# key_to_val_freq = {1: (1,1) 2: (2, 1), 3: (3, 1)}
# freq_to_keys = {1: OrderedDict([(1, None), (2, None), (3, None)])}
# min_freq = 1

lfu.put(4, 4) # evicts key 1
# key_to_val_freq = {2: (2, 1), 3: (3, 1), 4: (4, 1)}
# freq_to_keys = {1: OrderedDict([(2, None), (3, None)], [4, None])}
# min_freq = 1

print(lfu.get(2))
print(lfu.get(3))
# key_to_val_freq = {2: (2, 2), 3: (3, 2), 4: (4, 1)}
# freq_to_keys = {1: OrderedDict([(4, None)])
#                 2: OrderedDict([(2, None), (3, None)])}
# min_freq = 1

lfu.put(4,40)
# key_to_val_freq = {2: (2, 2), 3: (3, 2), 4: (40, 2)}
# freq_to_keys = {2: OrderedDict([(2, None), (3, None), (4, None)])}
# min_freq = 2

lfu.put(1, 1)
# key_to_val_freq = {3: (3, 2), 4: (40, 2), 1: (1,1)}  # evict (2,2)
# freq_to_keys = {1: OrderedDict([(1, None)])
#                 2: OrderedDict([(3, None), (40, None)])}

lfu.put(5, 5)
# key_to_val_freq = {3: (3, 2), 4: (40, 2), 5: (5,1)}  # evict (1,1).
# freq_to_keys = {1: OrderedDict([(5, None)])
#                 2: OrderedDict([(3, None), (40, None)])}
