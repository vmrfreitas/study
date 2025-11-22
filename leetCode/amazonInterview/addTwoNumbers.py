# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #result = ListNode()
        l1head = l1
        l2head = l2
        carry_over = 0
        result = 0
        while l1 and l2:
            result = l1.val + l2.val + carry_over
            print(result)
            if(result >= 10):
                result -= 10
                carry_over = 1
            else:
                carry_over = 0
            l1.val = result
            l2.val = result
            previousl1 = l1
            l1 = l1.next
            l2 = l2.next
        
        if(l1):
            while(l1 and (carry_over > 0)):
                print("entrei")
                l1.val += carry_over
                if (l1.val >= 10):
                    l1.val-=10
                    carry_over=1
                else:
                    carry_over = 0
                previousl1 = l1
                l1 = l1.next
            if(carry_over > 0):
                previousl1.next = ListNode(1)
            return l1head

        if(l2):        
            while(l2 and (carry_over > 0)):
                l2.val += carry_over
                if (l2.val >= 10):
                    l2.val-=10
                    carry_over=1
                else:
                    carry_over = 0
                previousl2 = l2
                l2 = l2.next
            if(carry_over > 0):
                previousl2.next = ListNode(1)
            return l2head
    
        if(carry_over > 0):
            previousl1.next = ListNode(1)
        
        return l1head
        