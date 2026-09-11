class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        if len(s) == 1: return s
        for i in range(len(s)):
            for x in (0, 1):
                rightPointer = i + x
                leftPointer = i
                while leftPointer > -1 and rightPointer < len(s) and s[leftPointer] == s[rightPointer]:
                    leftPointer -= 1
                    rightPointer += 1

                if (rightPointer - leftPointer) - 1 > len(longest):
                    longest = s[leftPointer + 1:rightPointer]

        return longest


            