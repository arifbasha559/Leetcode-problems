# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        stack = []
        current = head

        while current is not None:
            while stack and stack[-1].val < current.val:
                stack.pop()
            stack.append(current)
            current = current.next

        if not stack:
            return None

        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]

        stack[-1].next = None
        return stack[0]