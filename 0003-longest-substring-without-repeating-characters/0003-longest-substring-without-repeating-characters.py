class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        left=0
        freq={}
        res=0
        for right in range(n):
                
            freq[s[right]]=freq.get(s[right],0)+1
            while len(freq)<(right-left+1):
                freq[s[left]]=freq.get(s[left])-1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1
            if len(freq)==(right-left+1):
                res=max(res,right-left+1)
        return res 