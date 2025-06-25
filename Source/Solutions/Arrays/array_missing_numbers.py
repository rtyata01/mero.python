def find_missing_numbers_efficient(nums):
    if not nums:
        return []

    num_set = set(nums) # O(n), Remove duplicates to simplify gaps
    min_val = min(nums) # O(n), where n = len(nums)
    max_val = max(nums) # O(n),

    result = []
    for num in range(min_val + 1, max_val):
        if num not in num_set:
            result.append(num)

     # Calculate how many more missing numbers needed to match input length
    missing_count = len(nums) - (len(num_set) + len(result))
    
    if missing_count > 0:
        missing = range(max_val + 1, max_val + 1 + missing_count)
        result.extend(missing)
    
    return result

# Time complexcity = 3 * o(n) + o(m), where m = max-min = o(n + m)
# When the goal is to find missing numbers in a continuous range, set-based is better and it avoids the sorting complexity.

def find_missing_numbers(nums):
    if not nums:
        return []
    
    sorted_unique = sorted(set(nums))  # Remove duplicates to simplify gaps = o(n) + o(k log k)
    result = []

    # Find missing numbers between the sorted unique numbers
    for i in range(1, len(sorted_unique)):
        prev = sorted_unique[i - 1]
        curr = sorted_unique[i]
        missing = range(prev + 1, curr)
        result.extend(missing)

    # Calculate how many numbers are missing to match input size
    missing_count = len(nums) - len(sorted_unique) - len(result)
    
    if missing_count > 0:
        missing = range(sorted_unique[-1], sorted_unique[-1] + missing_count)
        result.extend(missing)    
    
    return result
# Time Complexity = o(n) + o(k log k) + o(m) = o(n log n + m)

nums =  [5,1,3,7,2,15,8]
print(f"Missing numbers array: ", find_missing_numbers(nums))
print(f"Missing numbers array: ", find_missing_numbers_efficient(nums))

nums =  [1,1]
print(f"Missing numbers array: ", find_missing_numbers(nums))
print(f"Missing numbers array: ", find_missing_numbers_efficient(nums))       
            
nums =  [1,1,2,2]
print(f"Missing numbers array: ", find_missing_numbers(nums))
print(f"Missing numbers array: ", find_missing_numbers_efficient(nums))       
            