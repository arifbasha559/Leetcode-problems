class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        
        nums.sort()
        res=[]
        for one in range(n-3):
            if one>0 and nums[one]==nums[one-1]:
                continue
            for two in range(one+1,n-2):
                if two>one+1 and nums[two]==nums[two-1]:
                    continue
                third = two+1
                four = n-1
                while third<four:
                    sum = nums[one]+nums[two]+nums[third]+nums[four]
                    if sum==target:
                        res.append([nums[one],nums[two],nums[third],nums[four]])
                        third+=1
                        four-=1
                        while third<four and nums[third]==nums[third-1]:
                            third+=1
                        while third<four and nums[four]==nums[four+1]:
                            four-=1
                    elif sum<target:
                        third+=1
                    else:
                        four-=1
        return res 