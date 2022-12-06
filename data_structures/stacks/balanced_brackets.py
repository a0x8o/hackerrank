#!/usr/bin/python

brackets = {')': '(', '}': '{', ']': '['}

n = int(raw_input().strip())

for _ in xrange(n):
    stack = []
    string = raw_input().strip()

    for char in string:
        if char in brackets.values():
            stack.append(char)
        elif len(stack) == 0 or brackets[char] != stack[-1]:
            stack.append(char)
            break
        else:
            stack.pop()
    
    if len(stack) > 0:
        print "NO"
    else:
        print "YES"

