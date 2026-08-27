import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^\w\d]", "", s).lower()
        frontP = 0
        endP = len(s) - 1
        while frontP <= endP:
            if s[frontP] != s[endP]: return False
            frontP += 1
            endP -= 1

        return True