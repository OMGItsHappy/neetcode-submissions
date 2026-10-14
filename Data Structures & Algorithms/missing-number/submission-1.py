class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        val = len(nums)
        for num in range(val):
            val ^= num

        for num in nums:
            val ^= num

        return val
