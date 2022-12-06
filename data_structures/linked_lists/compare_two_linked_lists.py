#!/usr/bin/python

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def compare_lists(headA, headB):
    if (not headA) and (not headB):
        return 1
    elif (not headA) or (not headB):
        return 0
    elif headA.data == headB.data:
        return compare_lists(headA.next, headB.next)
    else:
        return 0

