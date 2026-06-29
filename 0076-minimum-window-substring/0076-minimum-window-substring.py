class Solution:

    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        if n < m or m == 0:
            return ""

        # Frequency maps for what we need and what we currently have
        need = [0] * 128
        have = [0] * 128

        # Count unique characters needed from t
        unique_needed = 0
        for char in t:
            idx = ord(char)
            if need[idx] == 0:
                unique_needed += 1
            need[idx] += 1

        low = 0
        min_len = float("inf")
        start_idx = -1
        formed = 0  # Tracks how many unique characters meet the 'need' criteria

        for high in range(n):
            # Expand the window
            char_high = ord(s[high])
            have[char_high] += 1

            # If the current character frequency matches the required frequency
            if need[char_high] > 0 and have[char_high] == need[char_high]:
                formed += 1

            # Shrink the window from the left as long as it's valid
            while formed == unique_needed:
                current_len = high - low + 1

                # Update the minimum window tracking variables
                if current_len < min_len:
                    min_len = current_len
                    start_idx = low

                # Try to contract the window from the left
                char_low = ord(s[low])
                have[char_low] -= 1

                # If removing this character breaks the validity of the window
                if need[char_low] > 0 and have[char_low] < need[char_low]:
                    formed -= 1

                low += 1

        if min_len == float("inf"):
            return ""
        return s[start_idx : start_idx + min_len]