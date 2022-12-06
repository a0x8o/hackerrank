#!/usr/bin/python

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def reverse_print(head):
    data = []
    temp = head
    while temp:
        data.append(temp.data)
        temp = temp.next
    for i in range(len(data)):
        print(data[len(data)-i-1])

# better solution with recursive function

def reverse_print(head):
    if not head:
        return
    else:
        reverse_print(head.next)
    print head.data
