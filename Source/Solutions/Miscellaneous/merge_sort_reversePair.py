# count and find the reverse pairs, where 0 <= i < j <= n and nums[i] > 2 * nums[j]

def reversePairsWithList(nums):
    pairs = []

    def merge_sort(left, right):
        if left >= right:
            return 0
        mid = (left + right) // 2
        count = merge_sort(left, mid) + merge_sort(mid + 1, right)

        # Fix: Reset j for each i to correctly track all valid (i, j)
        for i in range(left, mid + 1):
            j = mid + 1
            while j <= right and nums[i] > 2 * nums[j]:
                pairs.append((nums[i], nums[j]))
                j += 1
            count += j - (mid + 1)

        # Merge step
        temp = []
        l, r = left, mid + 1
        while l <= mid and r <= right:
            if nums[l] <= nums[r]:
                temp.append(nums[l])
                l += 1
            else:
                temp.append(nums[r])
                r += 1
        while l <= mid:
            temp.append(nums[l])
            l += 1
        while r <= right:
            temp.append(nums[r])
            r += 1

        nums[left:right+1] = temp
        return count

    count = merge_sort(0, len(nums) - 1)
    return count, pairs

def reversePairsBruteForce(nums):
    count = 0
    pairs = []
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > 2 * nums[j]:
                count += 1
                pairs.append((nums[i], nums[j]))
    
    return count, pairs

nums = [1, 3, 4, 1]
count, pairs = reversePairsWithList(nums)
print("Count:", count)
print("Mergesort reverse Pairs (i, j):", pairs)

nums = [1, 3, 4, 1]
count, pairs = reversePairsBruteForce(nums)
print("Count:", count)
print("BruceForce reverse Pairs (i, j):", pairs)
