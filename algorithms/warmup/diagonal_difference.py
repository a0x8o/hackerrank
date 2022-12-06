#!/usr/bin/python

n = int(raw_input().strip())
sum = 0
for i in range(n):
    arr = map(int, raw_input().strip().split(' '))
    sum += (arr[i] - arr[n-i-1])

print abs(sum)

