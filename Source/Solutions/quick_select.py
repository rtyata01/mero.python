def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low <= high:
        pi = partition(arr, low, high)
        
        # If the pivot is the k-th smallest element
        if pi == k:
            return arr[pi]
        elif pi < k:
            return quickselect(arr, pi + 1, high, k)
        else:
            return quickselect(arr, low, pi - 1, k)
    return None

def find_kth_smallest(arr, k):
    # k is 1-indexed
    return quickselect(arr, 0, len(arr) - 1, k - 1)  # Convert to 0-indexed for quickselect

# Example Usage:
arr = [12, 3, 5, 7, 19, 1, 2, 10]
k = 4
print(f"The {k}th smallest number is: {find_kth_smallest(arr, k)}")
