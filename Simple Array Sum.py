#!/bin/python3

import os


#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#
import sys


def simpleArraySum(ar):
    # Write your code here
    n = 0
    for number in ar: #For no python já passa por toda a Array
        n = n + number
    return n


if __name__ == '__main__':
    fptr = sys.stdout

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()