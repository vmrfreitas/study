# given a sorted array with n elements that is rotated right (the end of the array goes to the beggining) by r positions, find a specific element in it.
from numpy import random


# just generating a random rotated array each time for testing purposes
randomArray = random.randint(100, size=(20)).tolist()
randomArray.sort()
rotation = random.randint(18)
if rotation == 0:
    array = randomArray
else:
    randomArray1 = randomArray[0:rotation]
    randomArray2 = randomArray[rotation:len(randomArray)]
    array = randomArray2 + randomArray1
# ------------------------------------------------------------------------


def findElement(element):
    rotationIndex = rotationSearch(0, len(array))
    if(rotationIndex != len(array)-1):
        array1 = array[0:rotationIndex+1]
        array2 = array[rotationIndex+1:len(array)]
        index = binarySearch(array1, 0, len(array1), element)
        if(index != -1):
            return index
        index = binarySearch(array2, 0, len(array2), element)
        if(index == -1):
            return index
        return index + rotationIndex + 1
    else:
        binarySearch(array, 0, len(array, element))
        return index
    

def binarySearch(localArray, minimum, maximum, element):
    pivotIndex = int((maximum - minimum)/2 + minimum)
    pivot = localArray[pivotIndex]
    if(pivot == element):
        return pivotIndex 
    if(len(localArray[minimum:maximum]) == 1):
        if(localArray[minimum] != element):
            return -1
        else:
            return minimum

    if pivot >=element:
        return binarySearch(localArray, minimum, pivotIndex, element)
    else:
        return binarySearch(localArray, pivotIndex, maximum, element)

def rotationSearch(minimum, maximum): # binary search to find the rotationIndex
    if(len(array[minimum:maximum]) == 1):
        return minimum

    pivotIndex = int((maximum - minimum)/2 + minimum)
    pivot = array[pivotIndex]
    if array[minimum] >= pivot:
        return rotationSearch(minimum, pivotIndex)
    else:
        return rotationSearch(pivotIndex, maximum)

print("The array is: ")
print(array)
element = input("Which element do you want to know the index of? ")
index = findElement(int(element))
if(index == -1):
    print("Element is not present on the array.")
else:
    print("The index is: " + str(index))
    print("Proof (array[index]): " + str(array[index]))