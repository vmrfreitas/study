# https://leetcode.com/problems/trapping-rain-water/?envType=company&envId=amazon&favoriteSlug=amazon-thirty-days-of-interviews

class Solution:
    def trap(self, height: List[int]) -> int:
        peaks = []
        largest_peak = 0
        right = 0
        left = 0
        result = 0
        while left < len(height)-1:
            if height[left] >= height[left + 1]: # found a peak
                left_peak = height[left]
                right = left + 1
                right_peak = 0
                right_location = right
                while right < len(height):
                    if(height[right]>height[right-1]):
                        if (height[right] >= right_peak):
                            right_location, right_peak = right, height[right]
                    if height[right] >= left_peak: # found next peak
                        break
                    right += 1
                # now we have the left peak and the right peak
                volume = min(left_peak, right_peak)
                while left <= right_location and left<len(height)-1:
                    water = volume - height[left]
                    if(water > 0):
                        result+= water 
                    left+=1
                left = right_location

            else:
                left += 1

        return result

# this solution ended up exceeding time limits on leetcode
# because it is O(N^2) in the worst case where the heights are in descending order
# as for each peak we may have to scan to the end of the list to find the next peak
# a better approach is to use two pointers, one at the start and one at the end
# and move the pointers towards each other, keeping track of the maximum height seen so far
# and calculating the water trapped at each position based on the minimum of the two maximums
# this approach is O(N) time and O(1) space
