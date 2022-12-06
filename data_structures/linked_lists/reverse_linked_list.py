#!/usr/bin/python

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def reverse(head):
    def private_reverse(prev, head):
        if not head:
            return prev
        else:
            temp = head.next
            head.next = prev
            return private_reverse(head, temp)
    return private_reverse(None, head)

