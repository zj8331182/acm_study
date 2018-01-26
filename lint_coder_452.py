"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    @param: head: a ListNode
    @param: val: An integer
    @return: a ListNode
    """

    def removeElements(self, head, val):
        if head is None:
            return None
        while head is not None and head.val == val:
            head = head.next
        if head is None:
            return None
        temp = head
        while temp.next is not None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(1)
    # c = ListNode(3)
    # d = ListNode(3)
    # e = ListNode(4)
    # f = ListNode(5)
    # g = ListNode(3)
    a.next = b
    # b.next = c
    # c.next = d
    # d.next = e
    # e.next = f
    # f.next = g

    s = Solution()
    h = s.removeElements(a, 1)
    while h is not None:
        print(h.val)
        h = h.next
