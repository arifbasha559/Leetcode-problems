class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}
        for val in magazine:
            freq[val] = freq.get(val, 0) + 1

        for val in ransomNote:
            try:
                if freq[val] == 0:
                    del freq[val]
                freq[val] -= 1
            except KeyError:
                return False
        return True