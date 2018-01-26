"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: the first node of linked list.
    @return: An integer
    """

    def countNodes(self, head):
        a = 0
        while head is not None:
            a += 1
            head = head.next
        return a
