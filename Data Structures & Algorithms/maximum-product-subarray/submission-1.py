class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxPrd = nums[0]
        minPrd = nums[0]
        largest = nums[0]

        for num in nums[1:]:
            tmp = maxPrd * num
            minPrd*=num

            maxPrd = max(tmp, minPrd, num)
            minPrd = min(minPrd, tmp, num)
            largest = max(maxPrd, minPrd, num, largest)

        return largest
