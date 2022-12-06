#!/usr/bin/python

# lesson: better to keep track of the maximum value instead of recomputing it
# each time

n = int(raw_input().strip())

stack = []
maximum = 0

for _ in xrange(n):
    query = map(int, raw_input().strip().split(' '))
    if query[0] == 1:
        stack.append(query[1])
        if query[1] > maximum:
            maximum = query[1]
    elif query[0] == 2:
        top = stack.pop()
        if maximum == top:
            if len(stack) > 0:
                maximum = max(stack)
            else:
                maximum = 0
    else:
        print(maximum)

