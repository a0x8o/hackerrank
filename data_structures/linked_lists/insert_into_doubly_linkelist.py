#!/usr/bin/python

class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

def sorted_insert(head, data):
    if not head:
        return Node(data)

    prev = head.prev
    cur = head

    while cur and (data > cur.data):
        prev = cur # can't put prev.next here since the first prev is None
        cur = cur.next

    new_node = Node(data, cur, prev)
    prev.next = new_node

    if cur: # else it's None and None doesn't have a prev field
        cur.prev = new_node
    
    return head

