# https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1115/
""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. """

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        num_index = 0

        for num in nums:
            try:
                num_map[num].append(num_index)
            except:
                num_map[num] = [num_index]
            num_index+=1

        for num in nums:
            if num in num_map:
                sum_num = target - num
                if sum_num == num:
                    if len(num_map[num]) > 1:
                        return [num_map[num][0], num_map[num][1]]
                elif (sum_num in num_map):
                    return [num_map[num][0], num_map[sum_num][0]]

# after seeing some answers I realized I didn't need two for loops 
# instead of checking if num is in map I could've checked if (target-num in map) and do it all in one loop
# complexity is the same tho.. copied from a faster time resolution:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if target-nums[i] in hashmap:
                ans = []
                ans.append(hashmap[target-nums[i]])
                ans.append(i)
                return ans
            hashmap[nums[i]] = i
        