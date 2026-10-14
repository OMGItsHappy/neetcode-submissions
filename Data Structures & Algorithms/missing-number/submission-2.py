class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        val = len(nums)
        for num in range(val):
            val ^= num ^ nums[num]

        return val
