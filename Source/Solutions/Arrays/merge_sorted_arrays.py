def merge_sorted_arrays(arr1, arr2):
    if not arr1 and not arr2:
        return []
    
    i, j = 0, 0
    result = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i +=1
        else:
            result.append(arr2[j])
            j +=1
    
    if i < len(arr1):
        result.extend(arr1[i:])
    
    if j < len(arr2):
        result.extend(arr2[j:])
        
    return result

# Time Complexity: O (n + m)
# Space Complexity: O (n + m)

import heapq
def heap_merge_sorted_arrays(arr1, arr2):
    return list(heapq.merge(arr1, arr2))

# Time Complexity: O (n + m)
# Space Complexity: O (n + m)

arr1 = [2, 2, 6, 8]
arr2 = [1, 3, 3, 5, 7, 9]
print(merge_sorted_arrays(arr1, arr2))  # Output: [1, 2, 2, 3, 3, 5, 6, 7, 8, 9]
print(heap_merge_sorted_arrays(arr1, arr2))

arr1 = [-2, 2, 4, 6, 8]
arr2 = [-1, 1, 3, 5, 7, 9]
print(merge_sorted_arrays(arr1, arr2))  # Output: [-2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(heap_merge_sorted_arrays(arr1, arr2))
