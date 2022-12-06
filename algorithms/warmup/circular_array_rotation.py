#!/usr/bin/python

n, k, q = map(int, raw_input().strip().split(' '))
arr = raw_input().strip().split(' ')

rot_arr = arr[-(k%n):] + arr[:-(k%n)]

for i in range(q):
    index = int(raw_input().strip())
    print rot_arr[index]

