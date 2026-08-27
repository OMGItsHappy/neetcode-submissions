from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        baseStr = " " * 26 * 2

        def produceString(sr):
            cnts = defaultdict(int)
            for letter in sr:
                cnts[letter] += 1
            baseStr = ""
            for char in range(ord("z") - ord("a") + 1):
                char = chr(char + ord("a"))
                baseStr += f"{char}{cnts[char]}"
            return baseStr

        res = defaultdict(list)
        for st in strs:
            res[produceString(st)].append(st)
        
        finalList = []
        for val in res.values():
            finalList.append(val)

        return finalList