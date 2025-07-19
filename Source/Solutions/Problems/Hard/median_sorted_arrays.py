# Hard: Given two sorted arrays A and B, with lengths m and n, find the median of the combined sorted array in O(log(min(m, n))) time.
# The median is the middle value in a sorted list of numbers.
# When even, the median is the midpoint between the two center values.

def find_median_sorted_arrays(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total = m + n
    half = (total + 1) // 2

    low, high = 0, m # length of shortest array.

    while low <= high:
        i = (low + high) // 2
        j = half - i

        left1 = float('-inf') if i == 0 else nums1[i - 1]
        right1 = float('inf') if i == m else nums1[i]
        left2 = float('-inf') if j == 0 else nums2[j - 1]
        right2 = float('inf') if j == n else nums2[j]

        if left1 <= right2 and left2 <= right1:
            if total % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) / 2
            else:
                return max(left1, left2)
        elif left1 > right2:
            high = i - 1
        else:
            low = i + 1

# Time Complexity: O(log(min(m, n))) – binary search on the shorter array.
# Space Complexity: O(1) 

print(f"Expected median: 2, Computed median: {find_median_sorted_arrays([1, 3], [2])}") 
print(f"Expected median: 4, Computed median: {find_median_sorted_arrays([1, 5, 6], [2, 4])}") 
print(f"Expected median: 4, Computed median: {find_median_sorted_arrays([1, 3, 5, 6], [2, 4])}") 
