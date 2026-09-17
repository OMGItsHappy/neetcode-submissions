class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}
        
        def sum(i, total):
            if i == len(nums):
                return total == target
            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = (sum(i + 1, total + nums[i]) + sum(i + 1, total - nums[i]))

            return dp[(i, total)]

        return sum(0, 0)