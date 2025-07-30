# Valid mountain array must have, 
# Length must be greater than 2

# There must be a single peak at index i such that:
# Increasing strictly before the peak: arr[0] < arr[1] < ... < arr[i]
# Decreasing strictly after the peak: arr[i] > arr[i+1] > ... > arr[n-1]


# single index, walk up to find peak and walk down.
# two pointer, walk up from left and down from right, to find the peak.

def valid_mountain_array(arr):
    n = len(arr)
    if n < 3:
        return False

    i = 0
    # Walk up
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1

    # Peak can't be first or last
    if i == 0 or i == n - 1:
        return False

    # Walk down
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1

    return i == n - 1

def valid_mountain_array(arr):
    n = len(arr)
    if n < 3:
        return False

    left, right = 0, n - 1

    while left + 1 < n and arr[left] < arr[left + 1]:
        left += 1

    while right - 1 >= 0 and arr[right - 1] > arr[right]:
        right -= 1

    return 0 < left == right < n - 1

print(f"Expected: False, Computed: ", valid_mountain_array([2, 1]))          # False (too short, or no increasing phase)
print(f"Expected: False, Computed: ", valid_mountain_array([3, 5, 5]))       # False (not strictly increasing)
print(f"Expected: True, Computed: ", valid_mountain_array([0, 3, 2, 1]))     # True (valid mountain)
print(f"Expected: True, Computed: ", valid_mountain_array([0, 2, 3, 2]))     # True (valid mountain)
print(f"Expected: False, Computed: ", valid_mountain_array([0, 2, 3, 2 , 1, 4, 5, 3, 2])) #False
