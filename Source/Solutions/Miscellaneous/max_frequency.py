from collections import Counter

def most_frequent_element(nums):
    if not nums:
        return None, 0

    counter = Counter(nums)  # dictionary
    element, count = counter.most_common(1)[0]
    return element, count

arr = [2, 1, 1, 1, 1, 2, 1, 2, 3, 1]
element, count = most_frequent_element(arr)
print(f"Element with max duplicates: {element}, Count: {count}")

# Time complexity = o (n) =  counter.most_common()

def most_frequent_element(nums):
    if not nums:
        return None, 0

    freq_map = {}  # dictionary 
    max_count = 0
    max_element = None

    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1
        
        if freq_map[num] > max_count:
            max_count = freq_map[num]
            max_element = num

    return max_element, max_count

arr = [2, 1, 1, 1, 1, 2, 1, 2, 3, 1]
element, count = most_frequent_element(arr)
print(f"Element with max duplicates: {element}, Count: {count}")

# Time complexity = o (n)