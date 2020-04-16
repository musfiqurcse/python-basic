#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mini = 0
    maxi = 0
    high = 0
    low = 0 
    for i in range(0,len(scores)):
        if i == 0:
            high = scores[i]
            low = scores[i]
        else:
            if high<scores[i]:
                high = scores[i]
                maxi +=1
            elif low>scores[i]:
                low = scores[i]
                mini +=1
    return maxi,mini


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
