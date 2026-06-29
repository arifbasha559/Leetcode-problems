
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        left = 0
        right = 0
        res1 = ""
        res2 = ""
        while left < len(s) and right < len(t):
            if s[left] == "#":
                res1 = res1[:  - 1]
            else:
                res1 = res1 + s[left]
            if t[right] == "#":
                res2 = res2[:  - 1]
            else:
                res2 = res2 + t[right]
            left += 1
            right += 1
        while left < len(s):
            if s[left] == "#":
                res1 = res1[:  - 1]
            else:
                res1 = res1 + s[left]
            left += 1
        while right < len(t):
            if t[right] == "#":
                res2 = res2[:  - 1]
            else:
                res2 = res2 + t[right]
            right += 1
        if res1 == res2:
            return True
        return False