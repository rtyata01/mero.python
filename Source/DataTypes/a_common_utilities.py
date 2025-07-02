from collections import deque, defaultdict, Counter
s_count = Counter("ababbc")
print(s_count)

text = "banana"
# defaultdict with int creates default 0 for new keys
letter_count = defaultdict(int)
for letter in text:
    letter_count[letter] += 1
print(dict(letter_count))

queue = deque()
queue.append('A')
queue.append('B')
print("Popped from left:", queue.popleft())     # 'A'
print("Queue after popleft:", queue)  # deque(['B', 'C'])

import heapq
nums = [5, 2, 3, 4]
heapq.heapify(nums)
smallest = heapq.heappop(nums)
heapq.heappush(nums, 7)

heap = [2]
smallest = heapq.heappop(heap)

from itertools import permutations, combinations, product, chain, combinations_with_replacement
# product(), permutations(), combinations(), combinations_with_replacement()
# groupby(), accumulate(), chain()

print(f"Permutations: ", list(permutations("abc")))

tasks = ['1', '2', '3']
print("Possible sequences of 2 tasks:")
for seq in permutations(tasks, 2):
    print(seq)

ingredients = ['Strawberry', 'Banana', 'Mango']
print("Possible 2-ingredient smoothie mixes (repeats allowed):")
for mix in combinations_with_replacement(ingredients, 2):
    print(mix)
    
players = ['Alice', 'Bob', 'Charlie', 'Diana']
print("Possible teams of 2 players:")
for team in combinations(players, 2):
    print(team)

from functools import lru_cache, reduce

import math
from math import gcd, sqrt, ceil, floor, log, factorial, isqrt
print("gcd(12, 18):", gcd(12, 18))  # 6 # gcd (greatest common divisor)
print("lcm(12, 18):", math.lcm(12, 18))  # 36 ##lcm (least common multiple) — available in Python 3.9+
print("sqrt(16):", sqrt(16))  # 4.0 # sqrt (square root)
print("ceil(3.7):", ceil(3.7))  # 4 # ceil (ceiling)
print("floor(3.7):", floor(3.7))  # 3 # floor
print("log(10):", log(10))  # ~2.302585 # log (natural logarithm)
print("factorial(5):", factorial(5))  # 120 # factorial
print("isqrt(17):", isqrt(17))  # 4  (since 4*4=16 <=17 and 5*5=25 >17) # isqrt (integer square root)


import bisect
pos = bisect.bisect_left([10, 20, 30, 40, 50], 30) # 2

import random
random_number = random.randint(1, 10)
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)

import re
text = "apple banana apricot avocado berry"
# Find all words starting with 'a'
matches = re.findall(r'\ba\w*', text)   # \b refers starts with i.e. boundary.
print("Words starting with 'a':", matches)

import string
string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'