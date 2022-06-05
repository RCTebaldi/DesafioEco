#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
# Write your code here
    resto = n % len(s) #define quantos caracteres sobram na cadeia de caracteres
    real = n // len(s) #define quantas vezes o grupo de caracteres pode ser inserida na cadeia de caracteres
    totalreal = s.count('a') * real #quantos 'a' tem na no grupo "cheio"
    totalresto = s[:resto].count('a') #quantos 'a' tem no que sobrou
    return (totalreal + totalresto)



if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
