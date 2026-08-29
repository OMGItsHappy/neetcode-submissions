class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < k: return k
        left = 0
        right = 0
        maxDigit = 0
        digitCounts = [0] * 26
        largest = 0

        while right < len(s):
            digitCounts[ord(s[right]) - ord("A")] += 1
            maxDigit = max(maxDigit, digitCounts[ord(s[right]) - ord("A")])
            while (right - left + 1) - maxDigit > k:
                digitCounts[ord(s[left]) - ord("A")] -= 1
                left += 1
            largest = max(largest, right-left + 1)
            right += 1
        print(digitCounts)
        return largest
                

            