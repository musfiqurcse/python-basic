#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the gridSearch function below.
def gridSearch(G, P,sr,sc,kr,kc):
    result = 'NO'
    for i in range(0,sr):
        for k in range(0,sc):
            if G[i][k] == P[0][0]:
                for n in range(0,kr):
                    check = False
                    for m in range(0, kc):
                        print(i+n,k+m)
                        if (i+n >= sr or k+m >= sc):
                            check = False
                            break
                        elif  G[i+n][k+m] != P[n][m]:
                            check = False
                            break
                        else:
                            check = True
                    if check == False:
                        result = 'NO'
                        break
                    else:
                        result = 'YES'
            if result == 'YES':
                break
        if result == 'YES':
            break
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P,R,C, r,c)

        fptr.write(result + '\n')

    fptr.close()
