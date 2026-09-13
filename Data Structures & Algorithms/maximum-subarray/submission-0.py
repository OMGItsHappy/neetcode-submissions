class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        i = 1
        res = nums[0]
        while i < len(nums):
            if currSum < 0:
                currSum = 0

            currSum += nums[i]
            res = max(res, currSum)
            i += 1

        return res