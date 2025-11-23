# I already did this one but here it is again using a iterative DFS


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if(not root):
            return True
        stack = []
        
        stack.append((root, float(inf), float(-inf)))
        
        while stack:
            (node, max_bound, min_bound) = stack.pop()
            val = node.val
            if(node.left):
                if(node.left.val >= node.val):
                    return False
                if(node.left.val <= min_bound):
                    return False
                stack.append((node.left, node.val, min_bound))
            if(node.right):
                if(node.right.val <= node.val):
                        return False
                if(node.right.val >= max_bound):
                    return False
                stack.append((node.right, max_bound, node.val))
        
        return True
    

    # apparently I could've just checked the bounds instead of checking the left/right values too,
    # but it is what it is
