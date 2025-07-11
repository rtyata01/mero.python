def find_error_nums(nums):
    n = len(nums)
    num_set = set()
    duplicate = -1

    for num in nums:
        if num in num_set:
            duplicate = num
        num_set.add(num)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    missing = expected_sum - (actual_sum - duplicate)
    
    return [duplicate, missing]


result = find_error_nums([1, 2, 2, 4])  # Output: [2, 3]
print(f"Expected: [2,3], Computed: {result}")
