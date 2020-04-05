#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(1,n+1,1):
        pi = " "*(n-i)
        si = "#"*i
        print(pi+si)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
