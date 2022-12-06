#!/usr/bin/python

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

nb_pos = 0
nb_neg = 0
nb_zer = 0

for i in arr:
    if i > 0:
        nb_pos += 1
    elif i < 0:
        nb_neg += 1
    else:
        nb_zer += 1

print float(nb_pos)/n
print float(nb_neg)/n
print float(nb_zer)/n

