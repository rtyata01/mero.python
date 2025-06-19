# Given unsorted array of integers numbs, return the length of the longest continuous increasing subsequence i.e. subarray. 
def longest_increasing_sequence(nums):
    if not nums:
        return 0
    
    longest = current = 1
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            current += 1
            longest = max(longest, current)
        else:
            current = 1
        
    return longest

def longest_increasing_sub_sequence(nums):
    if not nums:
        return 0

    max_len = 1
    current_len = 1
    start_index = 0
    max_start_index = 0

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_len += 1
        else:
            current_len = 1
            start_index = i  # New sequence starts here

        if current_len > max_len:
            max_len = current_len
            max_start_index = start_index

    return nums[max_start_index: max_start_index + max_len]


arr = [1, 3, 5, 4, 7]
print(f"Expected: 3, longest increasing sequence count: ", longest_increasing_sequence(arr))
result = longest_increasing_sub_sequence(arr)
print(f"Expected: 3, longest increasing sub sequence: {result}")

arr = [2, 2, 2, 2, 2]
print(f"Expected: 1, longest increasing sequence count: ", longest_increasing_sequence(arr))
result = longest_increasing_sub_sequence(arr)
print(f"Expected: 3, longest increasing sub sequence: {result}")

arr = [1, 3, 5, 4, 7, 8, 9, 15, 10, 17]
print(f"Expected: 5, longest increasing sequence count: ", longest_increasing_sequence(arr))
result = longest_increasing_sub_sequence(arr)
print(f"Expected: 3, longest increasing sub sequence: {result}")
    