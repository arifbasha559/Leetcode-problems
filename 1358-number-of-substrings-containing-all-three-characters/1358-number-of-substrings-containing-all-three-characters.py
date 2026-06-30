class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        for right in range(n): # Expand the window
            count[s[right]] += 1
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0: # Shrink the window
                res += n - right # All substrings ending at 'right' and starting from 'left' are valid
                count[s[left]] -= 1
                left += 1
        return res