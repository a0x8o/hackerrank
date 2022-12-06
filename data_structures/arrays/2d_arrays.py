#!/usr/bin/python

def generate_entries(i, j):
    return [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j), (i+1, j-1), (i+1, j), (i+1, j+1)]

arr = []
maximum = -63

for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

for i in xrange(1, 5):
    for j in xrange(1, 5):
        values = [arr[m][n] for m, n in generate_entries(i, j)]
        s = sum(values)
        if s > maximum:
            maximum = s

print(maximum)
