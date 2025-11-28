# https://leetcode.com/explore/interview/card/amazon/80/dynamic-programming/489/
# I knew this was a dinamyc programming problem but I couldn't figure it out,
# so I instinctively went for a expand from center approach, which I learned
# later that is actually a better approach memory-wise.
# But I botched it becauase I sliced the string in the recursive function,
# which is inefficient. I should've returned indices instead of slices.
# And also I should use a while function instead of recursion to avoid 
# hitting the recursion limit.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def search(left, right):
            if(left < 0 or right>=len(s)):
                return s[left+1:right]
            
            if(s[left] == s[right]):
                return search(left-1, right+1)
            else:
                return s[left+1:right]
        palindrome1 = ""
        palindrome2 = ""
        largest = ""
        for i in range(len(s)):
            palindrome1 = search(i-1, i)
            palindrome2 = search(i-1, i+1)
            largest = max(palindrome1, palindrome2, largest, key=len)
        
        if largest == "" and s != "":
            return s[0]
        return largest
