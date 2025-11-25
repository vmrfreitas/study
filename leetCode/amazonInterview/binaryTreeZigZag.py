# https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/2980/
# This one I refined with the help of my friend Gemini lol
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = [] 
        if(not root):
            return []
        queue = deque([(0, root)])
        result = []

        while queue:
            level, current = queue.popleft()
            
            if current.left:
                queue.append((level+1, current.left))
            if current.right:
                queue.append((level+1, current.right))   
                            
            try:
                result[level]
            except IndexError:
                result.append(deque()) 
            
            if level % 2 != 0:
                result[level].appendleft(current.val)
            else:
                result[level].append(current.val)
            
        return [list(d) for d in result]
