class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq={}
        for val in text:
            if val in "balloon":
                freq[val]=freq.get(val,0)+1
        needed = {
            "b": 1,
            "a": 1,
            "l": 2,
            "o": 2,
            "n": 1,
        }

        result = float("inf")
        for ch, count in needed.items():
            result = min(result, freq.get(ch, 0) // count)

        return result