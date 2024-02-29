# space complexity is a mess, probably very unoptimized, but I wanted to implement it and it works

import numpy as np
from numpy.random import randint


to_be_sorted =  randint(1,100,100).tolist() # random array of 100 elements, numbers ranging from 1 to 100
sorted_array = to_be_sorted.copy()

def quick_sort(subarray, start, end):
  if subarray:
    pivot = subarray[len(subarray)-1]
    pivot_index = 0
    subsubarray = []
    subsubarray.append(pivot)
    found = False
    for number in subarray:
      if number<pivot:
        subsubarray.insert(0,number)
        pivot_index+=1
      elif number>pivot:
        subsubarray.append(number)
      else:
        if found:
          subsubarray.insert(pivot_index,number)
        else:
          found = True
    
    sorted_array[start:end] = subsubarray
    quick_sort(subsubarray[:pivot_index].copy(), start, start + pivot_index)
    quick_sort(subsubarray[pivot_index+1:].copy(), start + pivot_index+1, end)

quick_sort(to_be_sorted.copy(), 0, len(to_be_sorted))
to_be_sorted.sort()
if to_be_sorted == sorted_array:
  print("it worked")