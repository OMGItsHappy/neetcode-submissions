class Solution:
    def __init__(self):
        self.none = "%20"

    def encode(self, strs: List[str]) -> str:
        if (len(strs) == 0): return self.none
        baseStr = ""
        for st in strs:
            for char in st:
                baseStr += str(ord(char)).rjust(3, "0")
            baseStr += " "
        return baseStr[:-1]

    def decode(self, s: str) -> List[str]:
        if s == self.none: return []
        strs = s.split(" ")
        resultStrings = []
        for st in strs:
            tmpStr = ""
            for num in range(0, len(st), 3):
                tmpStr += chr(int(st[num:num+3]))
            resultStrings.append(tmpStr)
        return resultStrings

