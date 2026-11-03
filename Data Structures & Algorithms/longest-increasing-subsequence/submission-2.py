class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1] * len(nums) for _ in range(len(nums))]
        def move(i, lastNum):
            if i >= len(nums):
                return 0
            if dp[i][lastNum + 1] != -1:
                return dp[i][lastNum + 1]
            longest = move(i + 1, lastNum) # Dont take
            if lastNum == -1 or nums[i] > nums[lastNum]:
                longest = max(longest, 1 + move(i + 1, i))
            dp[i][lastNum + 1] = longest
            return longest

        return move(0, -1)