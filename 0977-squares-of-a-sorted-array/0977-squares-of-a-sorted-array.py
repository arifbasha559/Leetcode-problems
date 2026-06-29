class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Create a result array of the same size
        result = [0] * n
        
        left = 0
        right = n - 1
        # Track where to place the next largest square (start from the back)
        write_index = n - 1
        
        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            
            # Compare which square is larger
            if left_square > right_square:
                result[write_index] = left_square
                left += 1  # Move left pointer inward
            else:
                result[write_index] = right_square
                right -= 1 # Move right pointer inward
                
            write_index -= 1 # Move our write target down
            
        return result