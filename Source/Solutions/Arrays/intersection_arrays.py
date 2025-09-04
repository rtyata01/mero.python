def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

def union(arr1, arr2):
    return list(set(arr1 + arr2))

def difference(arr1, arr2):
    return list(set(arr1) - set(arr2))

from collections import Counter

def intersection_with_duplicates(arr1, arr2):
    c1 = Counter(arr1)
    c2 = Counter(arr2)
    result = []

    for num in c1:
        if num in c2:
            # result.append([num] * min(c1[num], c2[num]))   [[2, 2], [3]]
            result.extend([num] * min(c1[num], c2[num]))  # [2, 2, 3]
    return result


arr1 = [4, 2, 3, 2, 1]
arr2 = [3, 2, 2, 5]

# print(union(arr1, arr2))  # Output: [1, 2, 3, 4, 5]
print(intersection(arr1, arr2))  # Output: [2, 3]
print(intersection_with_duplicates(arr1, arr2))  # Output: [2, 2, 3]