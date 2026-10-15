class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        res = ""
        stack.append([s[0], 1])
        for i in range(1, len(s)):
            if stack and stack[-1][0] == s[i]:
                if stack[-1][1] == k - 1:
                    stack.pop()
                else:
                    stack[-1][1] = stack[-1][1] + 1
            else:
                stack.append([s[i], 1])
        for i in stack:
            res += i[0] * i[1]
        return res