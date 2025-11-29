# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

import math

def overlapping_intervals(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    left = intervals[0][0]
    right = intervals[0][1]
    result = []
    for i in range(1,len(intervals)):
        interval = intervals[i]
        if(interval[0] <= right):
            right = max(right, interval[1])
        else:
            result.append([left,right])
            left = interval[0]
            right = interval[1]
    result.append([left,right])
    return result

# what is the time complexity of this approach?
# Time: O(N log N) where N is the number of intervals, due to the sorting step
# Space: O(N) in the worst case, if no intervals overlap, we store all intervals in the result
print(overlapping_intervals([[1, 10], [2, 3]]))
