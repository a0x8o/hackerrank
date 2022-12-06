#!/usr/bin/python

n = int(raw_input().strip())

for i in xrange(n):
    arr = [' ']*(n-i-1) + ["#"]*(i+1)
    print ''.join(arr)

