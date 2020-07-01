#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.

def repl(main_s, rep_c, idx):
    print(main_s)
    return main_s[:idx] + rep_c + main_s[idx+1:]

def bomberMan(r,c,n, grid):
    if n < 2:
        return grid
    new_g  = [ c*'O' for i in range(0,r)]
    if n < 3:
        return new_g
    else:
        for i in range(0,r):
            for j in range(0,c):
                if grid[i][j] == 'O':
                    new_g[i] = repl(new_g[i],'.',j)
                    if i-1>=0:
                        new_g[i-1] = repl(new_g[i-1],'.',j)
                    if i+1<r:
                        new_g[i+1]= repl(new_g[i+1],'.',j)
                    if j+1<c:
                        new_g[i] = repl(new_g[i],'.',j+1)
                    if j-1>=0:
                        new_g[i] = repl(new_g[i],'.',j-1)
        if n == 3 or ((n-3)/2)%2 != 0:
            return new_g
        else:
            return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(r,c, n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
