class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        left=0
        k=1
        checker=1
        while checker<len(nums):
            if nums[checker] ==nums[left]:
                checker+=1
            else:
                left+=1
                nums[left]=nums[checker]
                k+=1
                checker+=1  
        return k