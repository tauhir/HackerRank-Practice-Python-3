#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    bigarray = list(arr) #creating a clone array for the maximum sum
    mini = maxi = 0 #variables for sums
 
    for i in range(4): # range of 4 because the sum of 4 numbers are required as per spec
        small = min(arr) #get the min of the min array
        big = max(bigarray) #get the max of the max array
        mini += small           
        maxi += big
        arr.remove(small) #using list.remove() to remove the value added
        bigarray.remove(big)


    print(str(mini) + " " + str(maxi))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)