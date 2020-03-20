#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    string_split = s[:].split(' ')
    main_string = [ i[0].upper() + i[1:] if len(i)>0 else i for i in string_split]
    # main_string = [ i.capitalize() for i in string_split]
    # print(main_string)
    return ' '.join(main_string)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
