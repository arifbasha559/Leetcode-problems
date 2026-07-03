class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not A:
            return 0
            
        worst, beste, ans = nums[0], nums[0], nums[0]
        
        # Start from the second element
        for i in nums[1:]:
            v1, v2, v3 = i, beste * i, worst * i
            worst = min(v1, v2, v3)
            beste = max(v1, v2, v3)
            ans = max(ans, beste)
            
        return ans