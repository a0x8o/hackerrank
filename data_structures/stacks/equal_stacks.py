#!/usr/bin/python

# lesson: don't compute things you have already computed: be smart when implementing cumsum

_ = map(int, raw_input().strip().split(' '))
h0 = map(int, raw_input().strip().split(' '))
h1 = map(int, raw_input().strip().split(' '))
h2 = map(int, raw_input().strip().split(' '))

h0.reverse()
h1.reverse()
h2.reverse()

max_height = -1

def generate_cumsum(arr):
    total = 0
    for k in arr:
        total += k
        yield total

def cumsum(arr):
    return list(generate_cumsum(arr))

def get_maximum_and_index(arr):
    return max( [ (arr[i][-1], i) for i in xrange(len(arr)) ], key=lambda (value, index): value )

def are_same_values(arr):
    return arr[0][-1] == arr[1][-1] == arr[2][-1]

h = [cumsum(h0), cumsum(h1), cumsum(h2)]


while len(h[0]) > 0 and len(h[1]) > 0 and len(h[2]) > 0:
    maximum, index = get_maximum_and_index(h)
    if are_same_values(h):
        max_height = maximum
        break
    else:
        h[index].pop()

if max_height != -1:
    print(max_height)
else:
    print(0)

