class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diffTable = {}
        for i, num in enumerate(numbers):
            if num in diffTable:
                return [diffTable[num], i + 1]
            diffTable[target-num] = i + 1