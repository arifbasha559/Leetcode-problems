class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # code here
        left=0
        n= len(fruits)
        if n<1:
            return -1
        freq={}
        res=0
        for right in range(n):
            freq[fruits[right]]=freq.get(fruits[right],0)+1

            while len(freq)>2:
                freq[fruits[left]]-=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left+=1
            if len(freq)<=2:
                res=max(res,right-left+1)
        return res