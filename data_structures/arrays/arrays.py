#!/usr/bin/python

n = int(raw_input().strip())
arr = raw_input().strip().split()
rev = [arr[n-i-1] for i in range(n)]
print(" ".join(rev))
