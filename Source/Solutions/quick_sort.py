def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    pivot = arr[-1]  # Choose the last element as pivot (can also use random or median)
    left = [x for x in arr[:-1] if x <= pivot]  # All elements except the last one ≤ pivot
    right = [x for x in arr[:-1] if x > pivot]  # All elements except the last one > pivot

    return quick_sort(left) + [pivot] + quick_sort(right)

# Best or Average case Time Complexity: O(n log n)
# Worst case Time Complexity: O(n^2)

def quick_sort_in_place(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_in_place(arr, low, pi - 1)
        quick_sort_in_place(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Best or Average case Time Complexity: O(n log n)
# Worst case Time Complexity: O(n^2)

# Example Usage:
arr = [10, 3, 5, 7, 19, 1, 2, 12]
sorted_arr = quick_sort(arr) # [1, 2, 3, 5, 7, 10, 12, 19]
print(f"Sorted array: {sorted_arr}")

k = 4
print(f"The {k}th smallest number is: {sorted_arr[k-1]}")

quick_sort_in_place(arr, 0, len(arr) - 1)
print(f"In Place Sorted array: {arr}")
