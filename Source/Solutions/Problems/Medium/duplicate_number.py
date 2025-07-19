# Problem: Given an array with n + 1 integers where each integer is between 1 and n, find the duplicate.

def find_duplicate(nums):
    slow = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

# Time Complexity: O(n), Space Complexity: o(1) only constant, no other data structure used.

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
