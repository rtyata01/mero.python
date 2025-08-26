# Problem: Given an array with n + 1 integers where each integer is between 1 and n, find the duplicate.

# Floyd’s Tortoise and Hare (Cycle Detection)
def find_duplicate(nums):
    # Phase 1: Find intersection point in cycle
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Find entrance to cycle (duplicate number)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

# Time Complexity: O(n), 
# Space Complexity: o(1) only constant, no other data structure used.

def find_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

# Time Complexity: O(n)
# Space: O(n)

def find_duplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]
# Time Complexity: O(n log n) (due to sorting).
# Space: O(1) (if in-place sort allowed).

# Tests
input1 = [1, 1]
print("Input:", input1, "Output:", find_duplicate(input1))

input2 = [2, 2, 2, 2, 2]
print("Input:", input2, "Output:", find_duplicate(input2))

input3 = [1, 1, 2, 3, 4, 5]
print("Input:", input3, "Output:", find_duplicate(input3))

input4 = [1, 2, 3, 4, 5, 5]
print("Input:", input4, "Output:", find_duplicate(input4))

input5 = [1, 2, 2, 4, 5, 5]
print("Input:", input5, "Output:", find_duplicate(input5))
