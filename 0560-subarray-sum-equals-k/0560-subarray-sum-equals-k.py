class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq={0:1}
        res=0
        sum_of_i=0
        for i in range(len(nums)):
            sum_of_i+=nums[i]
            ques= sum_of_i-k
            if ques in freq:
                res+=freq[ques]
            freq[sum_of_i]=freq.get(sum_of_i,0)+1
        return res