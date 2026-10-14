class Solution:
    def reverseBits(self, n: int) -> int:
        val = 0
        for x in range(32):
            val = val | (((n & (1 << x)) > 0) << 31 - x)

        return val