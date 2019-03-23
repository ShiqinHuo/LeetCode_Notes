#### recursive

```python3
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        prev = None
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = prev
        return p
``` 

#### iterative


```python3
#         prev = None
#         cur = head
#         while cur:
#             _next = cur.next
#             cur.next = prev
#             prev = cur
#             cur = _next
#         return prev
```