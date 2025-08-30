# Rotate an array to the right by k steps, with efficient solution.

def rotate_right(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

def rotate_right_reverse(nums, k):
    n = len(nums)
    k %= n  # Normalize k
    
    # Helper function to reverse a portion of the list
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    reverse(nums, 0, n - 1)       # Reverse entire list
    reverse(nums, 0, k - 1)       # Reverse first k elements
    reverse(nums, k, n - 1)       # Reverse remaining elements
    
    return nums

# Time Complexity: O(n)

nums = [1, 2, 3, 4, 5, 6, 7]
result = rotate_right(nums[:], 3)
print(f"Input: {nums}, after right rotation by 3: ", result)

result = rotate_right(nums[:], 1)
print(f"Input: {nums}, after right rotation by 1: ", result)

result = rotate_right(nums[:], 7)
print(f"Input: {nums}, after rigth rotation by 7: ", result)

result = rotate_right(nums[:], 8)
print(f"Input: {nums}, after right rotation by 8: ", result)

nums = [1, 2, 3, 4, 5, 6, 7]
result = rotate_right_reverse(nums[:], 3)
print(f"Input: {nums}, after right rotation by 3 using reverse: ", result)

result = rotate_right_reverse(nums[:], 1)
print(f"Input: {nums}, after right rotation by 1 using revserse: ", result)

result = rotate_right_reverse(nums[:], 7)
print(f"Input: {nums}, after right rotation by 7 using reverse: ", result)

result = rotate_right_reverse(nums[:], 8)
print(f"Input: {nums}, after right rotation by 8 using reverse: ", result)





