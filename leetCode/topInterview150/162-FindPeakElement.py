# https://leetcode.com/problems/find-peak-element/?envType=study-plan-v2&envId=top-interview-150
# 162. Find Peak Element
# I first ended up with this super convoluted solution because I was checking both left AND right, I could've gone only to the larger side... 
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def binarySearch(startI, endI):
            pivotI = int((endI - startI)/2) + startI
            pivot = nums[pivotI]
            
            if pivotI == (len(nums) -1):
                if pivotI == 0:
                    return pivotI
                elif pivot > nums[pivotI - 1]:
                    return pivotI
                else:
                    return binarySearch(startI, pivotI)
            elif pivotI == 0:
                if pivot > nums[pivotI + 1]:
                    return pivotI
                else:
                    return binarySearch(pivotI+1, endI)
            elif pivot > nums[pivotI+1]: 
                if pivot > nums[pivotI-1]:
                    return pivotI
                else:
                    return binarySearch(startI, pivotI)
            else:
                return binarySearch(pivotI+1, endI)
        
        return binarySearch(0, len(nums))
    
   
        
