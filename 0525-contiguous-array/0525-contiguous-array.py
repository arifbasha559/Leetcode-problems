class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        current_sum = 0
        sum_indices = {0: -1}
        for i, num in enumerate(nums):
            current_sum += 1 if num == 1 else -1
            if current_sum in sum_indices:
                current_length = i - sum_indices[current_sum]
                max_length = max(max_length, current_length)
            else:
                sum_indices[current_sum] = i
                
        return max_length