class Solution:
    def climbStairs(self, n: int) -> int:
        n1 = 1
        n2 = 1
        i = 1
        while i < n:
            tmp = n2
            n2 += n1
            n1 = tmp
            i += 1
        
        return n2
