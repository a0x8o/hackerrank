#!/usr/bin/python

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# non memory-efficient solution
# - add each datum to a data array
# - at the end, we have all the values, the length of the linked list and the position
# - simple array indexing

def get_node_value_from_tail(head, position):
    data = []
    temp = head
    while temp:
        data.append(temp.data)
        temp = temp.next
    if len(data) == 0:
        return None
    else:
        return data[len(data)-position-1]

# memory-efficient solution but we do two passes
# - first pass: we first get the length of the linked list
# - second pass: stop at the right place

def get_node_value_from_tail(head, position):
    length = 0
    temp = head

    while temp:
        length += 1
        temp = temp.next
    
    if length == 0:
        return None
    
    i = 1
    temp = head

    while length-i-position > 0:
        temp = temp.next
        i += 1

    return temp.data

# memory-efficient solution with only one pass
# - create two pointers that are position nodes apart
# - increment both pointers until the first pointer reaches the end
# - the second pointer is the position-th from the tail

def get_node_value_from_tail(head, position):
    if not head:
        return None

    temp1 = head
    temp2 = head

    for i in range(position):
        temp1 = temp1.next

    while temp1.next:
        temp1 = temp1.next
        temp2 = temp2.next

    return temp2.data


