#!/usr/bin/python

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def insert_head(head, data):
    if not head:
        new_head = Node(data)
    else:
        new_head = Node(data, head)
    return new_head

