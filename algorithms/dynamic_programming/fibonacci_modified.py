#!/usr/bin/python

a, b, n = map(long, raw_input().strip().split(" "))
i = 3
temp = a + pow(b, 2)

while i < n:
    a = b
    b = temp
    temp = a + pow(b, 2)
    i += 1

print temp

