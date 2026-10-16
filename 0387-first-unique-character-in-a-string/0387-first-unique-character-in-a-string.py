from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = defaultdict()
        for i in s:
            freq[i] = freq.get(i,0)+1
        for i,v in enumerate(s):
            if freq[v]!=1:
                continue
            return i
        return -1