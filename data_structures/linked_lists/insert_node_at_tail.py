#!/usr/bin/python

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def insert_tail(head, data):
    if not head:
        head = Node(data)
    elif not head.next:
        head.next = Node(data)
    else:
        insert_tail(head.next, data)
    return head

