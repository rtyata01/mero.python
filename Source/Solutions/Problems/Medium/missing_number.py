# Given an unsorted array of n distinct numbers in the range [1, n], find the missing number.”

def find_missing_number(nums):
    if not nums:
        return None
    
    length = len(nums)
    unique_numbers = set(nums)
    
    for i in range(1, length + 1):
        if i not in unique_numbers:
            return i
        
    return length + 1

def find_missing(nums):
    n_min = min(nums)
    n_max = max(nums)
    num_set = set(nums)
    for i in range(n_min, n_max + 1):
        if i not in num_set:
            return i
    
    return n_max + 1 

# Only works for 1 missing number, starting from 1...N
# Does not work for negative number.
# Does not work for unsorted
def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

test_cases = [
    [0],
    [1],
    [1, 2, 3],
    [3, 0, 1],
    [1, 3, 5, 4],
    [-3, 0, -1],
    [4, 5, 7, 8, 9],
]

    
for i, input in enumerate(test_cases):
    print(f"Missing number: {find_missing_number(input)} in {input}")
    print(f"Missing number: {find_missing(input)} in {input}")
    if i <=3:
        print(f"Missing number: {missing_number(input)}")