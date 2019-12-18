#!/bin/python3

import math
import os
import random
import re
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys, height = 0, 0
    for step in s:
        if step == "D":
            height -= 1
        else:
            height += 1
            if height == 0:
                valleys += 1
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
