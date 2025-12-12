# https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/2985/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            def diam(node, longest):
                if not node:
                    return longest

                return max(diam(node.left, longest + 1), diam(node.right, longest + 1))

            nodes_with_childs = set()
            def dfs(node):
                if not node:
                    return
                if node.left and node.right:
                    nodes_with_childs.add(node)
                dfs(node.left)
                dfs(node.right)

            max_diam = 0
            dfs(root)
    
            for node in nodes_with_childs:
                diameter = diam(node.left,0) + diam(node.right,0)
                max_diam = max(max_diam, diameter)
            if root not in nodes_with_childs:
                max_diam = max(diam(root,0) - 1, max_diam) 

            return max_diam
    

# this mess of a solution got accepted but is not optimal at all
# the complexity of this is O(n^2) in the worst case because for each node with two childs
# we are calculating the depth of its left and right subtree again and again


# better solution with my friend copilot:
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update diameter at this node
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return height for parent
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.diameter
    

# basically calculates diameter on the fly for each node, and the height function returns the height of the tree
# so the parent node already knows the max height of each child subtree without recalculating it again