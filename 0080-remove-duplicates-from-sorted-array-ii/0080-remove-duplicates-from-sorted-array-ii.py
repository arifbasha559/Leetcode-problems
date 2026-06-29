class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        # 'left' is our write pointer. The first two elements are safe, 
        # so the next valid slot to write into starts at index 2.
        left = 2
        
        # 'checker' scans the rest of the array starting from index 2
        for checker in range(2, len(nums)):
            # If the current number is NOT equal to the number 2 slots behind 'left',
            # it means we haven't reached a 3rd duplicate yet. It's safe to keep!
            if nums[checker] != nums[left - 2]:
                nums[left] = nums[checker]
                left += 1
                
        return left
