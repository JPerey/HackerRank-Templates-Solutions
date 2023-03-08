#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def compareTriplets(a, b):
    # Write your code here
    i = 0
    score_list = [0, 0]
    for digit in a:
        if b[i] > digit:
            score_list[1] += 1
            i += 1
        elif b[i] < digit:
            score_list[0] += 1
            i += 1
        else:
            i += 1
    return score_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
