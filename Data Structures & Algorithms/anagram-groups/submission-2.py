from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        baseStr = " " * 26 * 2

        def produceString(sr):
            counts = [0] * 26
            for letter in sr:
                counts[ord(letter) - ord("a")] += 1
            return counts

        res = defaultdict(list)
        for st in strs:
            res[tuple(produceString(st))].append(st)
        
        finalList = []
        for val in res.values():
            finalList.append(val)

        return finalList