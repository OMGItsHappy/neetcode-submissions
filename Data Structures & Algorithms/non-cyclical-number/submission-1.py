class Solution:
    def isHappy(self, n: int) -> bool:
        def product(n):
            return sum(map(lambda x: int(x)**2, str(n)))
        slow, fast = n, product(n)

        while slow != fast:
            slow = product(slow)
            fast = product(product(fast))
        
        if slow == 1:
            return True
        return False