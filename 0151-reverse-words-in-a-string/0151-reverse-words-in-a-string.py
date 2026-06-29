class Solution:
    def reverseWords(self, s: str) -> str:
        raw = s.split(sep=' ')
        rev=""
        for i in raw:
            rev=f"{i} {rev}"
            rev=rev.strip()
        return rev