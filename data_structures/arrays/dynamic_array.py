#!/usr/bin/python

N, Q = map(int, raw_input().strip().split(' '))

seqList = [[] for i in xrange(N)]
lastAns = 0

for q in xrange(Q):
    i, x, y = map(int, raw_input().strip().split(' '))
    seq = (x ^ lastAns) % N
    if i == 1:
        seqList[seq].append(y)
    else:
        size = len(seqList[seq])
        lastAns = seqList[seq][y % size]
        print lastAns

