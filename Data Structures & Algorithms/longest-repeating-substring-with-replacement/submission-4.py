class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counts = defaultdict(int)
        mx = 0
        mostChars = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            mostChars = max(mostChars, counts[s[r]])

            while (r - left + 1) - mostChars > k:
                counts[s[left]] -= 1
                left += 1
            mx = max(mx, r-left + 1)
        return mx
            


