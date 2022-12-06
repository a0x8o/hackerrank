#!/usr/bin/python

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def remove_duplicates(head):
    if not head:
        return head

    prev = head
    temp = head.next

    while temp:
        if temp.data == prev.data:
            temp2 = temp
            temp = temp.next
            prev.next = temp
            del temp2
        else:
            prev = prev.next
            temp = temp.next
            
    return head

