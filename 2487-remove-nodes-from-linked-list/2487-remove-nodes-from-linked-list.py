# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head

        head.next = self.removeNodes(head.next)

        if head.next is not None and head.val < head.next.val:
            return head.next

        return head
