# Given array of nums n, where one number is duplicated and one number is missing. 
# Find the duplicate and missing number
    # if numbers start from 1 to n, then utilize sum formula = n * (n + 1) // 2 
# Works for both negative and positive.

def find_duplicate_missing_number(nums):
    
    unique_numbers = set(nums)
    actual_sum = sum(nums)
    duplicate = actual_sum - sum(unique_numbers)
    
    # Sum of expected unique values (excluding the duplicate)
    min_val = min(nums)
    max_val = max(nums)
    
   # Expand the range if needed so that it contains exactly 'expected_count' values
    while (max_val - min_val + 1) < len(nums):
        # Prefer expanding outward symmetrically if possible
        if (min_val - 1) not in unique_numbers:
            min_val -= 1
        else:
            max_val += 1

    expected_sum = sum(range(min_val, max_val + 1))
    
    missing = expected_sum - (actual_sum - duplicate)
    return duplicate, missing

# Tests
test_cases = [
    [1, 2, 2, 4],
    [2, 2, 4, 5, 6],
    [2, 3, 4, 5, 5],
    [-2, -2, 0, 1],
    [-5, -4, -2, -2],
]

for input in test_cases:
    duplicate, missing = find_duplicate_missing_number(input) 
    print(f"Input: {input}, Duplicate number: {duplicate}, Missing number: {missing}")

