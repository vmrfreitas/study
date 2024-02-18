# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
# 88. Merge Sorted Array
# This is not the best solution because list.insert actually has O(n) complexity... So this is not really O(n+m), but O(n²). Will try again.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j = 0
        i = 0
        inserted = 0
        while i < (n+m) and j < n:
            if nums1[i] > nums2[j]:
                inserted += 1
                nums1.insert(i, nums2[j])
                nums1.pop()
                j+=1
            if (i-inserted) >= m:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j+=1
            i+=1


# This is faster than my previous. I could've changed nums1 in place instead of using the extra array, though.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j = 0
        i = 0
        nums_extra = []
        not_stop = True

        while not_stop:
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    nums_extra.append(nums1[i])
                    i+=1
                else:
                    nums_extra.append(nums2[j])
                    j+=1
            else:
                if j < n:
                    nums_extra.append(nums2[j])
                    j+=1    
                elif i < m:
                    nums_extra.append(nums1[i])
                    i+=1
                else:
                    not_stop = False
        i = 0
        for num in nums_extra:
            nums1[i] = num
            i+=1