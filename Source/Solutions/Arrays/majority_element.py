def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate if nums.count(candidate) > len(nums) // 2 else None

from collections import Counter

def majority_element_counter(nums):
    counts = Counter(nums)
    num, count = counts.most_common(1)[0]  ## (1) → [(3, 3)]  ## (1)[0] → (3, 3)
    return num if count > len(nums) // 2 else None

arr = [2, 1, 1, 1, 1, 1, 2, 2, 3, 1]
print(majority_element(arr))  # Output: 1
print(majority_element_counter(arr))  # Output: 1

arr = [2, 1, 1, 1, 1, 1, 2, 2, 3, 3]
print(majority_element(arr))  # Output: None
print(majority_element_counter(arr))  # Output: 1
