#!/usr/bin/python

t = int(raw_input().strip())

# a little too much
for s in range(t):
    word = [c for c in raw_input().strip()]
    n = len(word)
    find_sup = False

    for i in xrange(n-1, -1, -1):
        arr = []
        for j in xrange(i+1, n):
            if word[j] > word[i]:
                arr.append(word[j])

        if len(arr) > 0:
            arr.sort()
            temp = word[i]
            word[i] = arr[0]
            index = word[(i+1):].index(arr[0])
            word[i+1+index] = temp
            end_word = word[(i+1):]
            end_word.sort()
            new_word = word[:(i+1)] + end_word
            find_sup = True
            print(''.join(new_word))
            break

    if not find_sup:
        print("no answer")

# much faster way
for s in range(t):
    word = list(raw_input().strip()) # no need for a list comprehension
    n = len(word)
    i = -1

    for j in xrange(n-1):
        if word[j] < word[j+1]:
            i = j

    if i == -1:
        print("no answer")
        continue
    
    k = i+1
    for j in xrange(i+2, n):
        if word[j] > word[i]:
            k = j

    temp = word[i]
    word[i] = word[k]
    word[k] = temp
    end_word = word[(i+1):]
    end_word.sort()
    print(''.join(word[:(i+1)] + end_word))

