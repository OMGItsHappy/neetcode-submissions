class Solution:
    def numDecodings(self, s: str) -> int:
        vals = [-1] * len(s)

        def naive(pos):
            if pos >= len(s):
                return 1
            if vals[pos] > -1:
                return vals[pos]
            if s[pos] == "0":
                vals[pos] = 0
                return 0
            res = naive(pos + 1)
            if pos < len(s) - 1 and (s[pos] != "0" and int(s[pos: pos+2]) < 27):
                res += naive(pos+2)
            vals[pos] = res
            return res


        return naive(0)