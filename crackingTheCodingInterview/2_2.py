from linked_list import LinkedList

input_list = LinkedList([2,5,6,7,8,34])

print(str(input_list))

# 0 is last, 1 is penultimate, etc
def return_kth_to_last(k):
    list_length = 0
    for node in input_list:
        list_length+=1
    index = 0
    for node in input_list:
        if(index == list_length-k-1):
            return node
        index+=1 

print(str(return_kth_to_last(1)))