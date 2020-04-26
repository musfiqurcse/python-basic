#!/bin/python3

import math
import os
import random
import re
import sys

def input_string(st):
    main_dicti = {}
    jj = []
    for i in st:
        if i not in main_dicti:
            main_dicti[i] = 1
        else:
            main_dicti[i]+=1 
    #  - sign used to descending order sort in lambda function
    jj = sorted(main_dicti.items(), key=lambda x:(-x[1],x[0]))
    for k in range(0,3):
        print(jj[k][0],jj[k][1])
        


if __name__ == '__main__':
    s = input()
    input_string(s)
