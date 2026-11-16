class Solution:
    def search(self,nums: list[int], target: int) -> int:
        n = len(nums)
        low,  high = 0,  n-1
        while low <= high:
            mid = low + (high - low) // 2
            curr = nums[mid]
            if curr == target:
                return mid
            elif curr < target:
                low = mid+1
            else:
                high = mid-1
        return -1