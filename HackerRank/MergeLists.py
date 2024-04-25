# https://www.hackerrank.com/challenges/one-week-preparation-kit-merge-two-sorted-linked-lists?utm_campaign=social-buttons&utm_medium=twitter&utm_source=challenge 

# Complete the mergeLists function below. Merge two lists to a sorted one.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

# revisiting now, kinda cheesy how I did this lmao
def mergeLists(head1, head2):
    
    # take the second element of the tuple, meaning the data, to use as key
    def takeSecond(elem):
        return elem[1]
    
    array_from_list = []
    
    # append every element of each list into an array of a tuple (head, data)
    while(head1 != None):
        array_from_list.append((head1, head1.data))
        head1 = head1.next
    while(head2 != None):
        array_from_list.append((head2, head2.data))
        head2 = head2.next
    # sort the array using the data as key
    array_from_list.sort(key=takeSecond)
    # get the head of the new merged list
    returning_head = array_from_list[0][0]
    # link the heads together
    for i in range(len(array_from_list)-1):
        array_from_list[i][0].next = array_from_list[i+1][0]
    return returning_head