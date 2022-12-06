#!/usr/bin/python

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

MAX_SIZE = 100

# hacky way using constraints
def has_cycle(head):
    temp = head
    length = 0
    while temp:
        length += 1
        temp = temp.next
        if length > MAX_SIZE:
            return True
    return False

# more general way without taking into account the max size: Floyd's algorithm
def has_cycle(head):
    if (not head) or (not head.next):
        return False

    tortoise = head
    hare = head.next

    while tortoise != hare:
        tortoise = tortoise.next
        if (not hare.next) or (not hare.next.next):
            return False
        hare = hare.next.next

    return True

# imporoved code
def has_cycle(head):
    turtoise = head
    hare = head

    while hare and hare.next:
        turtoise = turtoise.next
        hare = hare.next.next

        if turtoise == hare:
            return True

    return False
        
