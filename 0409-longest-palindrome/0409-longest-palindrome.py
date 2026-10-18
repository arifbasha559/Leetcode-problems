class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1

        ans=0
        odd=False
        for v in freq.values():
            if v%2==0:
                ans+=v
            else:
                odd=True
                temp=v-1
                ans+=temp
        if odd:
            ans+=1
        return ans

