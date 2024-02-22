# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
# 80. Remove Duplicates from Sorted Array II
# It ended up kinda convoluted by I ended up doing it fast and it is O(n) so I'm happy with it.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums) < 3):
            return len(nums)
        sizeOfNums = len(nums)
        stop = False
        i = 0
        
        while not stop:
            if(i<sizeOfNums-1):
                if(nums[i] == nums[i+1]):
                    if(i<sizeOfNums-2):
                        if(nums[i] == nums[i+2]):
                            del nums[i]
                            i-=1
                            sizeOfNums-=1
            else:
                stop = True
            i+=1

       
        return len(nums)
        