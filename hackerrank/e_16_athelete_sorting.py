import math
import os
import random
import re
import sys

counter = 0

def checker_item(elem):
    return elem[counter]

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []
    # Sorting after adding the list 
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    counter = k
    list_item = sorted(arr,key=checker_item)
    for i in range(0, n):
        res =""
        for k in range(0,m):
            res+="{0}".format(list_item[i][k])
            if k!=m-1:
                res+=" "
        print(res)
