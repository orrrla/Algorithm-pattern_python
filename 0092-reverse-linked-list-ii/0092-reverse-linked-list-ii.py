# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        pre=p0=ListNode(next=head)
        for _ in range(left-1):
            pre=pre.next
        dummy=None
        cur=pre.next
        for _ in range(right-left+1):
            nxt=cur.next
            cur.next=dummy
            dummy=cur
            cur=nxt
        pre.next.next=cur
        pre.next=dummy
        return p0.next