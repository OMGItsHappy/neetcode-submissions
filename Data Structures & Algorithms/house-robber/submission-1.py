class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)
        leftHouse = nums[0]
        rightHouse = nums[1]
        
        for right in nums[2:]:
            tmp = rightHouse
            rightHouse = max(leftHouse + right, rightHouse)
            leftHouse = max(tmp, leftHouse)

        return max(leftHouse, rightHouse)