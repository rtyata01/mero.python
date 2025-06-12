def merge_sort(arr):
    # Base case: an array with 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    # Merge two sorted arrays into one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add any remaining elements from left or right
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


arr = [5, 2, 9, 1, 6, 3, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 5, 6, 9]

# Time Complexity = O(n log n) = uses Divide and Conquer sorting algorithm.