class Solution:
    def countSubstrings(self, s: str) -> int:
        # Cover the base case of each char in str
        count = 0
        if len(s) < 2: return len(s)
 
        for i in range(len(s)):
            for x in [0, 1]:
                leftPointer = i
                rightPointer = i + x
                while leftPointer >= 0 and rightPointer < len(s) and s[leftPointer] == s[rightPointer]:
                    count += 1
                    leftPointer -= 1
                    rightPointer += 1
        return count
            
