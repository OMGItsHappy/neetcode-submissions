class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for x in range(len(nums))]
        suffix = [1 for x in range(len(nums))]

        for i, num in enumerate(nums):
            prefix[i] = num * (1 if i == 0 else prefix[i-1])
        for i in range(len(nums) -1, -1, -1):
            suffix[i] = nums[i] * (1 if i == len(nums) -1 else suffix[i+1])
        res = [suffix[1]]
        for i in range(0, len(nums) - 2):
            res.append(suffix[2 + i] * prefix[i])
        res.append(prefix[-2])


        return res