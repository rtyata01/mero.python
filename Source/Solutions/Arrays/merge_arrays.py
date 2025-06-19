def merge_unsorted(arr1, arr2):
    return list(set(arr1 + arr2))

def merge_unsorted_sorted(arr1, arr2):
    return sorted(set(arr1 + arr2))

def merge_unsorted_ordered(arr1, arr2):
    seen = set()
    result = []

    for num in arr1 + arr2:
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result

arr1 = [4, 4, 2, 2, 1]
arr2 = [3, 3, 2, 5]

print(merge_unsorted(arr1, arr2))  # Output: [1, 2, 3, 4, 5] (order may vary)

print(merge_unsorted_ordered(arr1, arr2))  # Output: [4, 2, 1, 3, 5]

print(merge_unsorted_sorted(arr1, arr2))  # Output: [1, 2, 3, 4, 5]

