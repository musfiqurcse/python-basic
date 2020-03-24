#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def bin_search(arr,item, maxi,mini):
    parti =(maxi+mini)//2
    if arr[mini] == item:
        return mini
    if arr[maxi] == item:
        return maxi
    if arr[mini]>item and arr[parti]<item:
        return bin_search(arr,item,parti,mini )
    else:
        return bin_search(arr,item,maxi,parti)
    
def sort_solution(arr, item,counter):
    li = len(arr) -1
    last = -1
    pos = 0
    found = -1
    for _ in range(0,len(arr)):
        if last != arr[li]:
            pos +=1
            last=arr[li]
        if (arr[li]>=item) and found ==-1:
            found=pos
            if arr[li] > item:
                found-=1
            if counter !=-1:
                pos = counter
                break
        li -=1
    return (pos +1 - found,pos) if found > -1 else (1,pos)

def find_pos(arr, item):
    arr.append(item)
    searchi = list(set(arr))
    searchi.sort(reverse=True)
    return bin_search(searchi, item, len(searchi)-1,0)

# Complete the climbingLeaderboard function below.

def climbingLeaderboard(scores, alice):
    res=[]
    b=list(Counter(scores).keys())
    print(b)
    temp=len(b)-1
    for a in alice:
        for i in range(temp,-1,-1):
            if b[i]>a:
                res.append(i+2)
                temp=i
                break  
            elif i==0:
                res.append(1)     
    return res






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

