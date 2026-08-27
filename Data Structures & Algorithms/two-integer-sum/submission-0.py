class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numCount = len(nums)
        for x in range(numCount):
            for y in range(numCount):
                if x == y: continue
                if nums[x] + nums[y] == target:
                    return [min(x, y), max(x, y)]