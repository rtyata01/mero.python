# Hard: Given two sorted arrays A and B, with lengths m and n, find the median of the combined sorted array in O(log(min(m, n))) time.
# When odd, the median is the middle value in a sorted list of numbers.
# When even, the median is the midpoint between the two center values.

def find_median_sorted_arrays(nums1, nums2):
    # Ensure binary search on the smaller array nums1
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    low, high = 0, m

    while low <= high:
        i = (low + high) // 2      # for search in nums1, biasing the mid point towards left.
        j = (m + n + 1) // 2 - i   # for search in nums2, biasing the mid point toward right i.e. + 1

        # Paritions
        maxLeft1 = nums1[i - 1] if i > 0 else float('-inf')
        minRight1 = nums1[i] if i < m else float('inf')
        maxLeft2 = nums2[j - 1] if j > 0 else float('-inf')
        minRight2 = nums2[j] if j < n else float('inf')

        # Check Paritions
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            if (m + n) % 2 == 0:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            else:
                return max(maxLeft1, maxLeft2)
        elif maxLeft1 > minRight2:
            high = i - 1
        else:
            low = i + 1

# Time Complexity: O(log(min(m, n))) – binary search on the shorter array.
# Space Complexity: O(1) 

def find_median_sorted_arrays_naive(nums1, nums2):
    # Step 1: Merge the two sorted arrays
    merged = sorted(nums1 + nums2)  # O(N log N) + time.
    
    n = len(merged)
    
    # Step 2: Compute the median
    if n % 2 == 1: 
        # Odd length → middle element
        return merged[n // 2]
    else:
        # Even length → average of two middle elements
        mid1 = merged[n // 2 - 1]
        mid2 = merged[n // 2]
        return (mid1 + mid2) / 2
    
# Naive merging approaches (O(m + n) log(m + n)), where you merge both arrays and then find medium.
    # merge = O(m + n) 
    # sort = o(N log N), where N = m + n.

print(f"Expected median: 2, Computed median: {find_median_sorted_arrays([1, 3], [2])}") 
print(f"Expected median: 4, Computed median: {find_median_sorted_arrays([1, 5, 6], [2, 4])}") 
print(f"Expected median: 4, Computed median: {find_median_sorted_arrays([1, 3, 5, 6], [2, 4])}") 

# [2 | 4]
# [1, 3 | 5, 6]
# max(left) + min(right) / 2 = 3 + 4 / 2 = 3.5

# i=(0+2)/2 = 1, 
# j= (2+4+1)/2 - i = 3-2= 2
# nums1: left = 2, right = 4
# nums2: left = [1,3] right = [5,6]
# 2 + 4 % 2==0, even, so median = max(2,3) + min(4, 5) / 2 = 3+4/2 = 3.5
