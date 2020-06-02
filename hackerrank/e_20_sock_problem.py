#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    countr = 0
    for i in range(0,n):
        if ar[i] != 0 and i+1 < n:
            for j in range(i+1, n):
                if ar[j] != 0  and ar[j] == ar[i]:
                    countr+=1
                    ar[j]=0
                    break
    return countr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
