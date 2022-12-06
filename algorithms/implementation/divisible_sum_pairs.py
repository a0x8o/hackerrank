#!/usr/bin/python

n, k = map(int, raw_input().strip().split(' '))
arr = map(int, raw_input().strip().split(' '))

count = 0

for i in range(n-1):
    for j in range(i+1, n):
        if (arr[i]+arr[j]) % k == 0:
            count += 1

print count

