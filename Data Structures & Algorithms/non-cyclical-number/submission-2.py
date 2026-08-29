class Solution:
    def isHappy(self, n: int) -> bool:
        def product(n):
            output = 0

            while n:
                digit = n % 10
                digit = digit ** 2
                output += digit
                n = n // 10
            return output
        slow, fast = n, product(n)

        while slow != fast:
            slow = product(slow)
            fast = product(product(fast))
        
        if slow == 1:
            return True
        return False