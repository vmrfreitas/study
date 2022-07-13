# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees
# code to check if given tree is a BST tree

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

# this is some code I was making that really didn't work out, put it here just to have it saved somewhere

def checkBST(root):
    if not root:
        return True
    root_value = root.data
    print(root_value)
    return_value = True
    
    def checkTree(node):
        if node.left:
            print(str(node.data) + "left" + str(node.left.data))
            if node.data > node.left.data and root_value > node.left.data:
                checkTree(node.left)
            else:
                return_value = False
        
        if node.right:
            print(str(node.data) + "right" + str(node.right.data))
            if node.data < node.right.data and root_value < node.right.data:
                checkTree(node.right)
            else:
                return_value = False

    checkTree(root)
    return return_value
    

# at the end my solution ended up like this:

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    tree_list = []
    
    if not root:
        return False
    
    def tree_to_list(node):
        if node.left:
            tree_to_list(node.left)
        tree_list.append(node.data)
        if node.right:
            tree_to_list(node.right)

    tree_to_list(root)

    sorted_no_repeats = sorted(list(dict.fromkeys(tree_list))) # reviewing it now I realize that instead of dict.fromkeys() I could just use set(), but whatever
    
    if sorted_no_repeats == tree_list:
        return True
    return False

# its an in-order dfs search to turn the tree into what should be a sorted list (if the tree was a BST)
# then just a conversion to dict and back to list to remove repeated numbers and vuala
        