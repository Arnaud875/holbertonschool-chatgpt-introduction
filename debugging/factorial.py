#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= n
    return result

f = factorial(int(sys.argv[1]))
print(f)