class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        val = 0
        res = []

        def add(i, total, curr):
            if total == target:
                res.append(curr.copy())
                return
            for j, num in enumerate(nums[i:]):
                newVal = total + num
                if newVal > target:
                    return
                curr.append(num)
                add(i + j, newVal, curr)
                curr.pop()
        add(0, 0, [])
        return res
            