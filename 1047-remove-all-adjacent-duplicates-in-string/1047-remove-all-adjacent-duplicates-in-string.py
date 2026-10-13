from collections import deque


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = deque()
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
                continue
            stack.append(i)
        return ''.join(stack)