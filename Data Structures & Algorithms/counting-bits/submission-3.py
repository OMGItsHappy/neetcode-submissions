class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        curr = 1
        while curr <= n:
            for x in range(min(curr, n - curr + 1)):
                res[curr + x] = 1 + res[x]
            curr *= 2

        return res

        