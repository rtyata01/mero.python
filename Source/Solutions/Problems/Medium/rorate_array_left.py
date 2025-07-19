# Rotate an array to the left by k steps, with efficient solution.

def rotate_left(nums, k):
    k %= len(nums)
    nums[:] = nums[k:] + nums[:k]
    return nums

def rotate_left_reverse(nums, k):
    n = len(nums)
    k %= n  # Normalize k
    
    def reverse(sub_nums, start, end):
        while start < end:
            sub_nums[start], sub_nums[end] = sub_nums[end], sub_nums[start]
            start += 1
            end -= 1
    
    reverse(nums, 0, k - 1)       # Reverse first k elements
    reverse(nums, k, n - 1)       # Reverse remaining n - k elements
    reverse(nums, 0, n - 1)       # Reverse the whole array
    
    return nums

# Time Complexity: O(n)

nums = [1, 2, 3, 4, 5, 6, 7]
result = rotate_left(nums[:], 3)
print(f"Input: {nums}, after left rotation by 3: ", result)

result = rotate_left(nums[:], 1)
print(f"Input: {nums}, after left rotation by 1: ", result)

result = rotate_left(nums[:], 7)
print(f"Input: {nums}, after left rotation by 7: ", result)

result = rotate_left(nums[:], 8)
print(f"Input: {nums}, after left rotation by 8: ", result)

nums = [1, 2, 3, 4, 5, 6, 7]
result = rotate_left_reverse(nums[:], 3)
print(f"Input: {nums}, after left rotation by 3 using reverse: ", result)

result = rotate_left_reverse(nums[:], 1)
print(f"Input: {nums}, after left rotation by 1 using revserse: ", result)

result = rotate_left_reverse(nums[:], 7)
print(f"Input: {nums}, after left rotation by 7 using reverse: ", result)

result = rotate_left_reverse(nums[:], 8)
print(f"Input: {nums}, after left rotation by 8 using reverse: ", result)



