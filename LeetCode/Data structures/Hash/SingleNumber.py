# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1176/
# returns the only non-duplicated number in the list
# could have used xor for fastertime, or could've used dict:
# try to pop number as key in dict
# if couldn't, add number to dict
# popitem() at the end to return the only element still in list

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_set = set()
        repeated_num_set = set()
        for num in nums:
            if (num in num_set):
                repeated_num_set.add(num)
            num_set.add(num)
        for num in nums:
            if (num not in repeated_num_set):
                return num

# did this one after checking some other attempts:

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            try:
                num_set.remove(num)
            except:
                num_set.add(num)
        return num_set.pop()

# not really faster tho, both of them being linear time 