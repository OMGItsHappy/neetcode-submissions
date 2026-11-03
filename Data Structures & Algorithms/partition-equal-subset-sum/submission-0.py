class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False
        total = total // 2
        def sub(i, currSum):
            if currSum == total:
                return True
            if i == len(nums) or currSum > total:
                return False

            return sub(i + 1, currSum + nums[i]) or sub(i + 1, currSum)
        
        return sub(0, 0)
