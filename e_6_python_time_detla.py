#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime, timedelta
def conv_auto(stp):
    # print(stp)
    i = -1
    if stp[0] == '-':
        i= 1
    res = i*(int(stp[1:3])*(60*60) + int(stp[3:])*60)
    # print(int(stp[3:])*60)
    return res

# Complete the time_delta function below.
def time_delta(t1, t2):
     d1 = datetime.strptime(t1[:-6],'%a %d %b %Y %H:%M:%S') + timedelta(seconds=conv_auto(t1[-5:]))
     d2 = datetime.strptime(t2[:-6],'%a %d %b %Y %H:%M:%S') + timedelta(seconds=conv_auto(t2[-5:]))
     res = int((d1 - d2).total_seconds())
     return str(res*-1 if res < 0 else res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
