#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.
def rotate_array(a, k):
    temp = a[k]
    a[k] = a[k+1]
    a[k+1] = a[k+2]
    a[k+2] = temp

def larryArrayMain(n, A):
    for i in range(0, n-2):
        for j in range(n-2-1, i-1, -1):
            while A[j] > A[j+1] or A[j] > A[j+2]:
                rotate_array(A, j)
    return "YES" if A[n-2] < A[n-1] else "NO" 
def larrysArrayPrimary(n, A):
    counter=0
    for i in range(0, n - 1 ):
        f1 =0
        f2 =0
        f3 =0
        if A[i] > A[i+1]:
            counter+=1
            if i+2 < n:
                f1=i
                f2=i+1
                f3 = i+2
            else:
                f1 = i - 1
                f2 = i
                f3 = i + 1
            print(f1,f2,f3)
            if A[f1] > A[f2] and A[f1] < A[f3] and A[f2] < A[f3]:
                return 'NO'
            elif A[f2] > A[f3] and A[f1] < A[f2] and A[f1] < A[f3]: 
                return 'NO'
            else: 
                continue
        elif counter > 1:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larryArrayMain(n, A)

        fptr.write(result + '\n')

    fptr.close()
