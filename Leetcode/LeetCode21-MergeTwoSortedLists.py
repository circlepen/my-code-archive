"""
Question:
Merge two sorted linked lists and return it as a new list. The new list should 
be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# iterative


def mergeTwoLists(l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
    dum = ListNode(None)
    prev = dum

    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next

    if l1 is None:
        prev.next = l2

    elif l2 is None:
        prev.next = l1

    return dum.next

# recursive


def mergeTwoLists(l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2


if __name__ == '__main__':
    dum = ListNode(None)
    dum.next = ListNode(1)
    curr = dum.next
    curr.next = ListNode(2)
    curr = curr.next
    curr.next = ListNode(4)

    dum2 = ListNode(None)
    dum2.next = ListNode(1)
    curr = dum2.next
    curr.next = ListNode(3)
    curr = curr.next
    curr.next = ListNode(4)

    ans = mergeTwoLists(dum.next, dum2.next)

    while ans.next:
        print(ans.val)
        ans = ans.next
    print(ans.val)
