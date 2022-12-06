#!/usr/bin/python

word = list(raw_input().strip())
cc = filter(lambda x: x.isupper(), word)
print len(cc)+1

