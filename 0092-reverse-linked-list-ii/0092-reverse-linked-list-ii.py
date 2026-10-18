# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        before_left = dummy

        for _ in range(left - 1):
            before_left = before_left.next

        sub_head = before_left.next

        # 4. Perform the link adjustments (right - left) times
        for _ in range(right - left):
            curr = sub_head.next
            sub_head.next = curr.next
            curr.next = before_left.next
            before_left.next = curr

        return dummy.next
