class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}
        for val in magazine:
            freq[val] = freq.get(val, 0) + 1

        for val in ransomNote:
            if freq.get(val, 0) == 0:
                return False
            freq[val] -= 1
            
        return True