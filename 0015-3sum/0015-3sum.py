class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        arr = []
        
        for i in range(len(nums)):
            # Bug 3 Fix: Skip duplicate values for the outer loop element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    arr.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Bug 1 & 2 Fix: ONLY skip duplicates after a successful match
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif current_sum < 0:
                    left += 1  # Sum is too small, make it bigger
                else:
                    right -= 1 # Sum is too big, make it smaller
                    
        return arr