from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for x in range(len(nums)):
            diff = target - nums[x]
            if nums[x] in diffs: return [diffs[nums[x]], x]
            diffs[diff] = x
