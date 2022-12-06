#!/usr/bin/python

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def merge_sorted_lists(headA, headB):
    if not headA:
        return headB
    elif not headB:
        return headA
    elif headA.data <= headB.data:
        headA.next = merge_sorted_lists(headA.next, headB)
        return headA
    else:
        headB.next = merge_sorted_lists(headA, headB.next)
        return headB

