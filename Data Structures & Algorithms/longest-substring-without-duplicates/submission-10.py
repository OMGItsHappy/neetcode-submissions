class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        right = 0
        
        seen = set()
        while right < len(s):
            longest = max(longest, right - left)
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            right += 1
            
        return max(longest, right - left)