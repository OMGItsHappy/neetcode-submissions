class Solution:
    def countSubstrings(self, s: str) -> int:
        # Cover the base case of each char in str
        count = len(s)
        if count < 2: return count

        for i in range(len(s)):
            leftPointer = i - 1
            rightPointer = i + 1
            while leftPointer >= 0 and rightPointer < len(s) and s[leftPointer] == s[rightPointer]:
                count += 1
                leftPointer -= 1
                rightPointer += 1

            leftPointer = i
            rightPointer = i + 1
            while leftPointer >= 0 and rightPointer < len(s) and s[leftPointer] == s[rightPointer]:
                count += 1
                leftPointer -= 1
                rightPointer += 1

        return count
            
