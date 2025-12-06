# https://leetcode.com/problems/copy-list-with-random-pointer/



"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if(not head):
            return None
        node = head
        head_copy = Node(head.val, None, None)
        node_copy = head_copy
        copy_hash = {}
        copy_hash[node] = node_copy
        while(node.next):
            node_copy.next = Node(node.next.val, None, None)
            copy_hash[node.next] = node_copy.next
            node_copy = node_copy.next
            node = node.next

        node = head
        node_copy = head_copy

        while(node):
            if(node.random):
                node_copy.random = copy_hash[node.random]
            node = node.next
            node_copy = node_copy.next

        return head_copy
