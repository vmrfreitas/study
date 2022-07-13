# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1105/
# return the elements present in both arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set()
        intersection_set = set()
        
        for num in nums1:
            nums1_set.add(num)
        for num in nums2:
            if (num in nums1_set):
                intersection_set.add(num)
        
        return list(intersection_set)

# after seeing other submissions:
# there are some more elegant solutions using - operations in set

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) - (set(nums1)-set(nums2)))