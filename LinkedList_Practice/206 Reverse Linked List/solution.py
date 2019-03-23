class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # recursive

    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        prev = None
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = prev
        return p

    # iterative

#         prev = None
#         cur = head
#         while cur:
#             _next = cur.next
#             cur.next = prev
#             prev = cur
#             cur = _next
#         return prev


# Recursion:

# def reverseList(self, head):
#     return self._reverse(head)
#
# def _reverse(self, node, prev=None):
#     if not node:
#         return prev
#     n = node.next
#     node.next = prev
#     return self._reverse(n, node)
