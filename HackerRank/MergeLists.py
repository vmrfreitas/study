# https://www.hackerrank.com/challenges/one-week-preparation-kit-merge-two-sorted-linked-lists?utm_campaign=social-buttons&utm_medium=twitter&utm_source=challenge 

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    
    def takeSecond(elem):
        return elem[1]
    array_from_list = []
    
    while(head1 != None):
        array_from_list.append((head1, head1.data))
        head1 = head1.next
    while(head2 != None):
        array_from_list.append((head2, head2.data))
        head2 = head2.next
    
    array_from_list.sort(key=takeSecond)
    returning_head = array_from_list[0][0]
    for i in range(len(array_from_list)-1):
        array_from_list[i][0].next = array_from_list[i+1][0]
    return returning_head