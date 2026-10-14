class Solution:
    def countBits(self, n: int) -> List[int]:
        def countBits(n):
            mask = 1
            count = 0
            while mask <= n:
                print(mask)
                count += (mask & n) > 0                
                mask = mask << 1

            return count

        res = []
        for i in range(n + 1):
            res.append(countBits(i))
        return res