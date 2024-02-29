# given two arrays of integers, A and B, for each element of B return how many numbers of A are lesser or equal than it
# for example:
# A = [1,2,3]
# B = [2,4]
#
# result = [2,3]
# explanation: for the first number of B, which is 2, there are 2 numbers of A that are lesser or equal than it: 1 and 2, so the return is 2
# for the second number of B, which is 4, there are 3 numbers of A that are lesser or equal than it: 1, 2 and 3, so the return is 3
# the returns are then appended to the result list: [2,3]


# example input
A = [2,3,4,53]
B = [5, 1, 55, 56,2,2,2,2] 
# expected result = [3, 0, 4, 4, 1, 1, 1, 1]

sortedB = []
for i,b in enumerate(B):
    sortedB.append((b, i)) # this is to not lose the original position of the B elements

sortedB.sort() # we sort the numbers first, then we will be going through both arrays at the same time
A.sort()

i, j = 0, 0
result = 0
b_index = 0
while True:
    if j>=len(B): # exit condition
        break
    if i==len(A): # we reached the end of A, but there are still numbers in B
        B[sortedB[j][1]] = result # so we just keep adding result again and again
        j+=1
    elif A[i] <= sortedB[j][0]: # found a number in A lesser than B
        result+=1 # increase the counter
        i+=1 # go to the next number in A
    else: # we're at a number in A that is larger than B
        B[sortedB[j][1]] = result # now we add the counter to the correct position in the result array (in this case I'm using B again)
        j+=1 # go to the next number in B

print(B) # the result is in B, since we had to preserve where the numbers were

# complexity would be O(n+m) where n is len(A) and m is len(B), but since we sorted first then it is O(nlog(n))