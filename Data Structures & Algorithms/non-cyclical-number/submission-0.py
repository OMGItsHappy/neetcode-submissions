class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def product(n):
            return sum(map(lambda x: int(x)**2, str(n)))

        while n not in seen and n != 1:
            seen.add(n)
            n = product(n)
        
        if n == 1:
            return True
        return False