def longest_consecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Only start counting if it's the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count the length of the current consecutive sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


def longest_consecutive_sorted(nums):
    if not nums:
        return 0

    nums.sort()  # Sort the array first
    longest_streak = 1
    current_streak = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue # Skip duplicates
        elif nums[i] == nums[i - 1] + 1:
            current_streak += 1
        else:
            longest_streak = max(longest_streak, current_streak)
            current_streak = 1

    return max(longest_streak, current_streak)


nums = [12, 6, 100, 4, 200, 1, 3, 2]
# Time complexity is o(n)
print(longest_consecutive(nums))  # Output: 4 (because of [1, 2, 3, 4])

# Time complexity is o(n log n)
print(longest_consecutive_sorted(nums))  # Output: 4 (because of [1, 2, 3, 4])