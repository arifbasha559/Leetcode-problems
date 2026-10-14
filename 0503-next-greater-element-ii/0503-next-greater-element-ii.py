class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        # Loop twice to simulate circular array
        for i in range(2 * n - 1, -1, -1):
            current_num = nums[i % n]
            
            while stack and stack[-1] <= current_num:
                stack.pop()
                
            if stack:
                res[i % n] = stack[-1]
                
            stack.append(current_num)
            
        return res