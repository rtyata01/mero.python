def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    # Validation step
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None

arr = [2, 1, 1, 1, 1, 1, 2, 2, 3, 1]
print(majority_element(arr))  # Output: None