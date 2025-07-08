def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickselect(arr, low, high, k):
    while low <= high:
        pivot_index = partition(arr, low, high)
        if k == pivot_index:
            return arr[k]
        elif k > pivot_index:
            low = pivot_index + 1
        else:
            high = pivot_index - 1
    return None

def find_kth_smallest(arr, k):
    if not 1 <= k <= len(arr):
        raise ValueError("k must be between 1 and the length of the array")
    return quickselect(arr, 0, len(arr) - 1, k - 1)

# Example Usage:
arr = [12, 3, 5, 7, 19, 1, 2, 10]
k = 4
print(f"The {k}th smallest number is: {find_kth_smallest(arr, k)}")
