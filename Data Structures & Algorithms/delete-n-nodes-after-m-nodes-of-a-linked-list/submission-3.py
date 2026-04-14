# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev, cur = head, head
        while cur and cur.next:
            c1 = 0
            while cur and c1 < m - 1:
                cur = cur.next
                c1 += 1
            if not cur:
                break
            nxt = cur.next
            for _ in range(n):
                if nxt:
                    nxt = nxt.next
            cur.next = nxt
            cur = nxt
        return head