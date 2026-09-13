class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [None] * len(nums)

        def jump(i):
            if dp[i] is not None: return dp[i]
            allowedJumps = nums[i]
            if allowedJumps + i >= len(nums) - 1:
                return True
            while allowedJumps > 0:
                if nums[i + allowedJumps] != 0:
                    if jump(i + allowedJumps):
                        return True
                allowedJumps -= 1
            dp[i] = False
            return False

        return jump(0)