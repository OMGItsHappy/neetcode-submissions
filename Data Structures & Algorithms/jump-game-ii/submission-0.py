class Solution:
    def jump(self, nums: List[int]) -> int:
        numberOfNums = len(nums)
        dp = [10e6] * numberOfNums
        dp[-1] = 0

        for i in range(numberOfNums - 2, -1, -1):
            end = min(numberOfNums, i + nums[i] + 1) # exclusive
            for j in range(i + 1, end):
                dp[i] = min(dp[i], 1 + dp[j])
        return dp[0]