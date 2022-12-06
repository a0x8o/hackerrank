#!/usr/bin/python

t = int(raw_input().strip())

for _ in range(t):
    n, k = map(int, raw_input().strip().split(' '))
    arr = map(int , raw_input().strip().split(' '))
    c = len(filter(lambda x: x <= 0, arr))
    if c >= k:
        print("NO")
    else:
        print("YES")

