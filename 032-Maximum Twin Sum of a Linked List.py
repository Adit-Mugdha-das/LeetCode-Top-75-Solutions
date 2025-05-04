# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        while slow:
            nnode=slow.next
            slow.next=prev
            prev=slow
            slow=nnode
        msum=0
        first=head
        sec=prev
        while sec:
            msum=max(msum,first.val+sec.val)
            first=first.next
            sec=sec.next
        return msum

'''SOLVED BY ADIT MUGDHA DAS'''