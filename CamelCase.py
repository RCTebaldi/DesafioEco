#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Write your code here
    padraoescrita = re.compile('^[a-z]|[A-Z]') #docRegex: https://www.w3schools.com/python/python_regex.asp
    t = padraoescrita.findall(s)
    return len(t)


if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
