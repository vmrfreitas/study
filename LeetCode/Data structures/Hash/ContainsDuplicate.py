# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1112/
# returns True if there's at least one duplicated number on the list

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if(num in num_set):
                return True
            num_set.add(num)
        return False