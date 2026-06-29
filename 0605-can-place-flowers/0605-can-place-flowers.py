class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        # If no flowers need to be planted, we are automatically done!
        spaces = 0
        
        streak = 1
        for f in flowerbed:
            if f == 0:
                streak += 1
            else:
                streak = 0

            if streak == 3:
                spaces += 1
                streak = 1

        if streak == 2:
            spaces += 1

        return spaces >= n