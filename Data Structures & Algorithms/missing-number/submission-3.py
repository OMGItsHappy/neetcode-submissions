class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = sum(range(len(nums) + 1))
        for num in nums:
            res -= num

        return res
