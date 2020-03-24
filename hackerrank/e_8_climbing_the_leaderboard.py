#!/bin/python3

import math
import os
import random
import re
import sys

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

def find_pos(arr, item):
    arr.append(item)
    searchi = list(set(arr))
    searchi.sort(reverse=True)
    return bin_search(searchi, item, len(searchi)-1,0)

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    result = []
    for i in alice:
        res= find_pos(scores,i)
        result.append(res+1)
    return result

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

