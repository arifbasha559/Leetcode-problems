class Solution:
    def maxAbsoluteSum(self,nums):
        max_end = max_sum = float('-inf')
        min_end = min_sum = float('inf')

        curr_max = curr_min = 0

        for x in nums:
            curr_max = max(x, curr_max + x)
            max_sum = max(max_sum, curr_max)

            curr_min = min(x, curr_min + x)
            min_sum = min(min_sum, curr_min)

        return max(abs(max_sum), abs(min_sum))
