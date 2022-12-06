#!/usr/bin/python

class Node(objec():
    def __init__(self, data=None, next_node= None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

def reverse(head):
    if not head:
        return head
    
    prev = head.prev
    cur = head

    while cur:
        temp = cur.next
        cur.prev = temp
        cur.next = prev
        prev = cur
        cur = temp

    return prev

