class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                digit = n % 10
                n//=10
                total_sum += digit ** 2
            return total_sum
        slow = fast = n
        while fast!=1:
            slow=get_next(slow)
            fast=get_next(get_next(fast))
            if slow==fast and slow!=1:
                return False
        return True
             

