class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while right > left:
            leftVal = numbers[left]
            rightVal = numbers[right]
            if leftVal + rightVal > target:
                right -= 1
            elif leftVal + rightVal < target:
                left += 1
            else:
                return [left + 1, right + 1]
        