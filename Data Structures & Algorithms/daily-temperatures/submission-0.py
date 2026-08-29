class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        if len(temperatures) < 2:
            return res
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            digit = temperatures[i]
            if len(stack) < 1 or stack[-1][0] <= digit:
                while len(stack) > 0 and stack[-1][0] <= digit:
                    stack.pop()
                if (len(stack) < 1): res[i] = 0
                else: res[i] = stack[-1][1] - i
            elif len(stack) > 0 and stack[-1][0] > digit:
                if len(stack) < 1: res[i] = 0
                else: res[i] = stack[-1][1] - i
            stack.append((digit, i))
        return res
            
        