#!/usr/bin/python

n, d = map(int, raw_input().strip().split(' '))
arr = raw_input().strip().split(' ')

if n == d:
    print(" ".join(arr))
else:
    new_arr = [arr[(i+d) % n] for i in xrange(n)]
    print(" ".join(new_arr))

