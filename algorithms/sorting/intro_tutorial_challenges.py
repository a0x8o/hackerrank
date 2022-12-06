#!/usr/bin/python

v = int(raw_input().strip())
n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

index = -1
for i in range(n):
    if arr[i] == v:
        index = i
        break

print(index)

