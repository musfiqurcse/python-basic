#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    hor = []
    ver = []
    leni = len(container)
    for i in range(0,leni):
        hor.append(sum(container[i]))
        sumi = 0
        for j in range(0,leni):
            sumi+=container[j][i]
        ver.append(sumi)
    hor.sort()
    ver.sort()
    if hor == ver:
        return "Possible"
    return "Impossible"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
