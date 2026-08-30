class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        s1Counts = {}
        s2Counts = {}
        matches = 0

        for i in range(len(s1)):
            s1Counts[s1[i]] = s1Counts.get(s1[i], 0) + 1
            s2Counts[s2[i]] = s2Counts.get(s2[i], 0) + 1

        for i in range(26):
            char = chr(ord("a") + i)
            matches += s1Counts.get(char, 0) == s2Counts.get(char, 0)

        for i in range(len(s1), len(s2)):
            if matches == 26: return True
            s2Counts[s2[i - len(s1)]] = s2Counts.get(s2[i-len(s1)], 0) - 1
            if s2Counts.get(s2[i - len(s1)]) == s1Counts.get(s2[i - len(s1)], 0):
                matches += 1
            elif s2Counts.get(s2[i - len(s1)]) == s1Counts.get(s2[i - len(s1)], 0) - 1:
                matches -= 1

            s2Counts[s2[i]] = s2Counts.get(s2[i], 0) + 1
            if s2Counts.get(s2[i]) == s1Counts.get(s2[i], 0):
                matches += 1
            elif s2Counts.get(s2[i]) == s1Counts.get(s2[i], 0) + 1:
                matches -= 1

        return matches == 26
            
