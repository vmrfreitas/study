# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/?envType=study-plan-v2&envId=top-interview-150
# 373. Find K Pairs with Smallest Sums
# at first my solution looked like this, which is O(n²):
from collections import defaultdict 
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairsDict = defaultdict(list)
        for num1 in nums1:
            for num2 in nums2:
                pairsDict[num1+num2].append([num1, num2])

        returnSums = []
        
        for sum1 in sorted(pairsDict.keys()):
            returnSums += pairsDict[sum1]
            if len(returnSums) >= k:
                return returnSums[:k]

# but this exceeded the memory limit since I had to add every combination because I had no idea which to remove when adding a new one
# then I created the following solution using heap:

from collections import defaultdict 
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairsHeap = []
        
        for num1 in nums1:
            for num2 in nums2:
                if(len(pairsHeap)>=k):
                    heapq.heappushpop(pairsHeap, (-(num1+num2), [num1, num2]))
                else:
                    heapq.heappush(pairsHeap, (-(num1+num2), [num1, num2]))

        returnSums = []
        for pair in pairsHeap:
            returnSums.append(pair[1])
        return returnSums
    
# but this exceeded the time limit... since now it is taking O(n²log(n²))... because popping and pushing to the heap is log(n)
# I had to look at other solutions to come up with the final answer:
    

from collections import defaultdict 
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairsHeap = []
        for num1 in nums1:
            heapq.heappush(pairsHeap, ((num1 + nums2[0]), 0))
        
        returnSums = []
        for _ in range(k): # comments are showing an example of the first iteration
            if(not pairsHeap):
                break

            summ, index2 =  heapq.heappop(pairsHeap) # since both the arrays are sorted, nums1[0] + nums2[0] will always be the smallest
            value2 = nums2[index2]
            returnSums.append([summ-value2, nums2[index2]])
            next_index2 = index2 + 1

            if next_index2 < len(nums2): # now since we popped out nums1[0] + nums2[0], we will calculate nums1[0] + nums2[1], and so on and so forth 
                heapq.heappush(pairsHeap, ((summ-value2) + nums2[next_index2], next_index2)) # by just doing sum - value2 (which is nums2[0]) we get nums1[i]
                                                                                             # without needing to know the value of i, then we add the next nums2
                                                                                             # which is nums2[1] in this case
            
        return returnSums
    
# I found it genious once I understood it lol, this reduces the problem to O((n+k)log(n+k))