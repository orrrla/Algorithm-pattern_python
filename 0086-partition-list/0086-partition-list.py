# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        p=dummy1=ListNode()
        q=dummy2=ListNode()
        cur=head
        while cur:
            if cur.val<x:
                p.next=cur
                p=p.next
            else:
                q.next=cur
                q=q.next
            cur=cur.next
        p.next=None
        q.next=None
        p.next=dummy2.next
        return dummy1.next
            