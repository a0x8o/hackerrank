#!/usr/bin/python

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def delete(head, position):
    if not head:
        return None
    elif position == 0:
        temp = head.next
        del head
        return temp
    else:
        head.next = delete(head.next, position-1)
        return head

