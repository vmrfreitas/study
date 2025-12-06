# https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/507/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftlist = []
        rightlist = []
        if not root:
            return True
        
        def dfs(node, left, direction):
            if not node:
                return
            
            if left:
                dfs(node.left, left, 0)
                leftlist.append((node.val, direction))
                dfs(node.right, left, 1)
            else:
                dfs(node.right, left, 0)
                rightlist.append((node.val, direction))
                dfs(node.left, left, 1)
        
        if(not root.left):
            if(not root.right):
                return True
            else:
                return False

        dfs(root.left, True, 0)
        dfs(root.right, False, 0)
        
        if(leftlist == rightlist):
            return True
        else:
            return False

# Time: O(N) where N is the number of nodes in the tree, since we visit each node once
# Space: O(N) because I am storing the values of all nodes in the left and right subtrees
# I saw a solution where they just did a recursive comparison of the left and right subtrees without storing the values, that would be better
