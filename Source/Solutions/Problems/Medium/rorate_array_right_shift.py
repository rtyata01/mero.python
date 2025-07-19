# Rotate an array to the right by k steps, using right shift, less efficient.

def rotate_right_shift(nums, k):
    n = len(nums)
    k %= n  # Normalize k
    
    for _ in range(k):
        # Save last element
        last = nums[-1]
        
        # Shift all elements right by one
        for i in range(n - 1, 0, -1):
            nums[i] = nums[i - 1]
        
        # Place last element at the front
        nums[0] = last
    return nums

# Time Complexity = O(n * k)

nums = [1, 2, 3, 4, 5, 6, 7]
result = rotate_right_shift(nums[:], 3)
print(f"Input: {nums}, after right rotation by 3 using shift: ", result)

result = rotate_right_shift(nums[:], 1)
print(f"Input: {nums}, after right rotation by 1 using shift: ", result)

result = rotate_right_shift(nums[:], 7)
print(f"Input: {nums}, after right rotation by 7 using shift: ", result)

result = rotate_right_shift(nums[:], 8)
print(f"Input: {nums}, after right rotation by 8 using shift: ", result)





