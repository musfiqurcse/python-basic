#!/bin/python3

from math import sqrt
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    leng = len(s)
    po = int(sqrt(leng))
    l = po if po*po == leng else po+1
    ss = ""
    for i in range(0,l):
        ss+=s[i]
        for j in range(i+l,leng,l):
            if j > leng -1:
                break
            ss+=s[j]
        if i+1 != l:
            ss+=" "
    return ss

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
