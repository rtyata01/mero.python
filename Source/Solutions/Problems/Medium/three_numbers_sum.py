# Problem: Given an array nums, return all triplets that sum up to zero.

def three_sum(nums, target=0):
    if not nums or len(nums) < 3:
        return []
    
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        # Skip duplicate values for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == target: 
                result.append([nums[i], nums[left], nums[right]])

                # Move left and right pointers to the next unique values, to skip duplicates
                left_val, right_val = nums[left], nums[right]
                while left < right and nums[left] == left_val:
                    left += 1
                while left < right and nums[right] == right_val:
                    right -= 1

            elif total < target:
                left += 1
            else:
                right -= 1

    return result

# Total Time Complexity: O(n²)
    # Sorting: O(n log n)
    # Looping and searching: O(n²)
# Space Complexity: O(1) (excluding output)

def three_sum_unsorted(nums):
    result = set()
    n = len(nums)

    for i in range(n):
        seen = set()
        for j in range(i + 1, n):
            complement = - (nums[i] + nums[j])
            if complement in seen:
                triplet = tuple(sorted((nums[i], nums[j], complement)))  # sorted to avoid duplicates (1, -1, 0) and (0, 1, -1)
                result.add(triplet)  # set will store unique.
            seen.add(nums[j])

    return [list(triplet) for triplet in result]

# Total Time Complexity: O(n²)
# Space Complexity: O(n²) - more space.

# Tests
input1 = [-1, 0, 1, 2, -1, -4]
print("Input:", input1, "Sum zero Output:", three_sum_unsorted(input1)) # Output: [[-1, -1, 2], [-1, 0, 1]]

input2 = []
print("Input:", input2, "Sum zero Output:", three_sum(input2)) # Output: []

input3 = [0, 1]
print("Input:", input3, "Sum zero Output:", three_sum(input3)) # Output: []

input4 = [0, 0, 0, 0]
print("Input:", input4, "Sum zero Output:", three_sum(input4)) # Output: [[0, 0, 0]]

input5 = [1, 2, -2, -1]
print("Input:", input5, "Sum zero Output:", three_sum(input5)) # Output: []

input6 = [-2, 0, 0, 2, 2]
print("Input:", input6, "Sum zero Output:", three_sum(input6)) # Output: [[-2, 0, 2]]