from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        counts = defaultdict(int)
        for i in range(len(s)):
            counts[s[i]] += 1
            counts[t[i]] -= 1
        return not any(counts.values())