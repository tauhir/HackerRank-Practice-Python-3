#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # The aim of this function is to use string manipulation and an if statement to 
    # change the format of the time
    array = list(s)
    hour = s[0]+s[1] 
    ampm = s[8]+s[9]
    
    if ampm == "AM":
        if hour == "12": 
            hour = "00"
        return hour+"".join(array[2:8]) 
    else:
        hour = int(hour)+12
        if hour == 24: 
            hour = 12
        hour = str(hour)
        if len(hour)==1:
            hour = "0" + hour
        return hour+"".join(array[2:8])



if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
