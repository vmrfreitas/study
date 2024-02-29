# https://leetcode.com/problems/same-tree/submissions/
# check if the two given binary trees are the same

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def tree_to_list(node, tree_list):
            if node:
                tree_list.append(node.val)
                if node.left:
                    tree_to_list(node.left, tree_list)
                else:
                    tree_list.append(None)
                if node.right:
                    tree_to_list(node.right, tree_list)
                else:
                    tree_list.append(None)
            else:
                tree_list.append(None)
        
        p_list = []
        tree_to_list(p, p_list)
        q_list = []
        tree_to_list(q, q_list)
        
        if p_list == q_list:
            return True
        else:
            return False

# basically just a pre-order depth-first search to make a list of the trees, then compare the lists
# a faster solution, gotten from leetCode, skipped the part of making a list and just compared node by node, during a depth-first search as well:

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)