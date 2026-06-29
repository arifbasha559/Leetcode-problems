class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                # 1. Update the smallest value found so far
                first = num
            elif num <= second:
                # 2. Update the second smallest value found so far
                second = num
            else:
                # 3. If a number is greater than BOTH, we found our triplet!
                return True
                
        return False