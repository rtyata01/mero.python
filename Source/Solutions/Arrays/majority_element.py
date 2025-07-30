# find the majority element in a list — that is, an element that appears more than ⌊n/2⌋ times in the list of length n. 
# If no such element exists, they return None.

def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate if nums.count(candidate) > len(nums) // 2 else None

from collections import Counter

def majority_element_counter(nums):
    counts = Counter(nums)
    num, count = counts.most_common(1)[0]  ## (1) → [(3, 3)]  ## (1)[0] → (3, 3)
    return num if count > len(nums) // 2 else None

from collections import defaultdict

def majority_element_one_pass_with_count(nums):
    count_map = defaultdict(int)
    majority_count = len(nums) // 2
        
    for num in nums:
        count_map[num] += 1
        if count_map[num] > majority_count:
            return num
    return None


arr = [2, 1, 1, 1, 1, 1, 2, 2, 3, 1]
print(majority_element(arr))  # Output: 1
print(majority_element_counter(arr))  # Output: 1

arr = [2, 1, 1, 1, 1, 1, 2, 2, 3, 3]
print(majority_element(arr))  # Output: None
print(majority_element_counter(arr))  # Output: 1
