#!/usr/bin/python

from math import sqrt
from scipy.stats import mode

N = int(raw_input().strip())
data = map(float, raw_input().strip().split(" "))
data.sort()

mean = sum(data) / N

median = (data[N/2-1] + data[N/2]) / 2 if N % 2 == 0 else data[(N-1)/2]

""" manual way to find the mode
count = 0
temp_count = 1
temp_mode = data[0]

i = 1
while i < N:
    if data[i] == data[i-1]:
        temp_count += 1
    else:
        if temp_count > count:
            temp_mode = data[i-1]
            count = temp_count
            temp_count = 1

mode = int(data[-1]) if temp_count > count else int(temp_mode)
"""

# scipy way to find the mode
mode = int(mode(data)[0][0])

std = round(sqrt(sum(map(lambda x: pow(x-mean, 2), data)) / N), 1)

lower_bound = mean - 1.96 * std / sqrt(N)
upper_bound = mean + 1.96 * std / sqrt(N)

print(round(mean, 1))
print(round(median, 1))
print(mode)
print(std)
print("{} {}".format(round(lower_bound, 1), round(upper_bound, 1)))

