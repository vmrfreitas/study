# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# from collections import defaultdict

# def top_n(nums, k):
#     top_count = defaultdict(lambda:0)
#     for num in nums:
#         top_count[num] += 1
#     top_count_list = sorted(top_count.keys, key=lambda x: top_count[x])
#     return top_count_list[0:k]

import heapq
from collections import defaultdict

def top_n(nums, k):
    top_count = defaultdict(lambda:0)
    for num in nums:
        top_count[num] += 1
    h = []
    # a min-heap of size k
    # as we iterate through the counts, we add to the heap
    # if the heap is already size k, we pop the smallest count
    # this makes sure we only keep the top k counts in the heap
    # as they dont require return in order, we can just return the keys from the heap

    for key, value in top_count.items():
        if(len(h) == k):
            heapq.heappushpop(h, (value, key))
        else:
            heapq.heappush(h, (value, key))
    return [key for value, key in h]

# what is the complexity of this approach?
# Time: O(N log k) where N is the number of elements in nums
# why log k? because we maintain a heap of size k, and each insertion/deletion operation on the heap takes O(log k) time
# Space: O(N) for the count dictionary and O(k) for the heap

print(top_n([10, 10, 10, 1, 2, 3], 1))
