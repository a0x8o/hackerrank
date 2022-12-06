#!/usr/bin/python

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def find_merge_node(headA, headB):
    """
    The easiest way would be to go the end of both lists then move backwards until
    data values diverge: the merge point is the precedent one.

    Unfortunately with linked list we can't do that. One way to mimic the first
    solution would be to reverse both lists then move forward until data values
    diverge: the merge point is the precedent one. The problem with this approach
    is that we need to create two new lists. Space complexity is not that great.

    On the other hand both solutions do pretty much the same thing: they compare
    the last element of list A with the last element of list B and so on moving
    backwards. We already know that moving backwards is hard with linked list, so
    our last hope is to simply move forward while comparing the right element of
    list A with the right element of list B. We can do that by 'aligning' our
    lists (by moving forward the right pointer the right number of times). Now
    we simply need a way to find the merge point. How do we do that?

    The merge point is unique since:
        - it has the same value in list A and list B
        - each element after the merge point will also have the same value in list
        A and list B
    
    We can use those two characteristics to find the merge point: after aligning
    both list (we now consider that all previous elements of the longest list are
    discarded), compare the first elements: if they are the same then this value
    might be the merge point so consider it as a temporary merge point. If they
    are different then that value can't be the merge point. Then check the second
    elements. If those are different then that means the temporary merge point
    (which might be null at this point) is not the actual merge point, so discard it.
    If they are the same then that means the temporary merge point might still be
    the real merge point (if it is not null). Procede recursively until the end of
    lists is reached.

    We are sure to find a merge point since constraints say so.
    """
    lenA = 0
    lenB = 0

    temp = headA
    while temp:
        lenA += 1
        temp = temp.next

    temp = headB
    while temp:
        lenB += 1
        temp = temp.next

    tempA = headA
    tempB = headB

    if lenA >= lenB:
        for i in range(lenA-lenB):
            tempA = tempA.next
    else:
        for i in range(lenB-lenA):
            tempB = tempB.next

    m = None

    while tempA:
        if tempA.data == tempB.data:
            if not m:
                m = tempA.data
        else:
            m = None

        tempA = tempA.next
        tempB = tempB.next
    
    return m

