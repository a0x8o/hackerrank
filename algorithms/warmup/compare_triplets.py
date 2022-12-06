#!/usr/bin/python

a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))

scoreA = 0
scoreB = 0

for i, j in zip(a, b):
    if i > j:
        scoreA +=1
    elif j > i: 
        scoreB += 1

print("{} {}".format(scoreA, scoreB))

