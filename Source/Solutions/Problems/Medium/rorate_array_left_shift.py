# Rotate an array to the right by k steps, using left shift, less efficient.

def rotate_left_shift(nums, k):
    n = len(nums)
    k %= n  # Normalize k
    
    for _ in range(k):
        # Save the first element
        first = nums[0]
        
        # Shift all elements left by one
        for i in range(1, n):
            nums[i - 1] = nums[i]
        
        # Place the first element at the end
        nums[-1] = first
    
    return nums

# Time Complexity: O (n * k)

nums = [1, 2, 3, 4, 5, 6, 7]
result = rotate_left_shift(nums[:], 3)
print(f"Input: {nums}, after left rotation by 3 using shift: ", result)

result = rotate_left_shift(nums[:], 1)
print(f"Input: {nums}, after left rotation by 1 using shift: ", result)

result = rotate_left_shift(nums[:], 7)
print(f"Input: {nums}, after left rotation by 7 using shift: ", result)

result = rotate_left_shift(nums[:], 8)
print(f"Input: {nums}, after left rotation by 8 using shift: ", result)



