import math
import os
import random
import re
import sys

nm = input().split()

n = int(nm[0])

m = int(nm[1])

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())

def sorting(elm):
    return elm[k]

arr.sort(key=sorting)
for i in range (len(arr)):
    x= ' '.join(map(str,arr[i]))
    print(x)