class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        beste,ans=-float('inf'),-float('inf')
        for i in nums:
            v1,v2= beste+i,i
            beste=max(v1,v2)
            ans=max(beste,ans)
        return ans