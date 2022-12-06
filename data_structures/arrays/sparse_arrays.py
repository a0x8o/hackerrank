#!/usr/bin/python

# with arrays, use no built-in methods except append

words = []
freq = []

n = int(raw_input().strip())

for i in range(n):
    word = raw_input().strip()
    if i == 0:
        words.append(word)
        freq.append(1)
    else:
        find_word = 0
        for j in range(len(words)):
            if words[j] == word:
                freq[j] += 1
                find_word = 1
                break
        if find_word == 0:
            words.append(word)
            freq.append(1)

q = int(raw_input().strip())

for i in range(q):
    word = raw_input().strip()
    find_word = 0
    for j in range(len(words)):
        if words[j] == word:
            find_word = 1
            print(freq[j])
            break
    if find_word == 0:
        print(0)

# with a map

from collections import defaultdict

words = defaultdict(int)

n = int(raw_input().strip())
for i in range(n):
    word = raw_input().strip()
    words[word] += 1

q = int(raw_input().strip())
for i in range(q):
    word = raw_input().strip()
    print(words[word])
