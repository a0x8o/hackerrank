#!/usr/bin/python

x1, r1, x2, r2 = map(int, raw_input().strip().split(' '))

if r2 >= r1:
    print "NO"
else:
    diff = x2 + r2 - x1 - r1
    while diff > 0:
        diff += (r2 - r1)
    if diff == 0:
        print "YES"
    else:
        print "NO"

