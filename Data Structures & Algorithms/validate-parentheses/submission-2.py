class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        values = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        for char in s:
            if char in values.values():
                stack.append(char)
            elif len(stack) > 0 and values.get(char) == stack[-1]:
                stack.pop()
            else: return False
        return len(stack) == 0
        