class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # Initialize the output array with 1s
        res = [1] * n
        # Pass 1: Calculate the Prefix products (Left side)
        # res[i] will store the product of all numbers to the left of i
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Calculate Suffix products and multiply them in-place
        # We walk backwards from the end of the array
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res