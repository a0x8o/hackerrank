#!/usr/bin/python

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def insertNth(head, data, position):
    if position == 0:
        return Node(data, head)
    elif position == 1:
        new_node = Node(data, head.next)
        head.next = new_node
        return head
    else:
        insertNth(head.next, data, position-1)
        return head

