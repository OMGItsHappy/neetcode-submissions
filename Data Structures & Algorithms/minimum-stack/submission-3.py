class MinStack:

    def __init__(self):
        self.arr = []
        

    def push(self, val: int) -> None:
        mn = min(val, self.arr[-1][1] if self.arr else val)
        self.arr.append([val, mn])
        

    def pop(self) -> None:
        self.arr.pop()
        

    def top(self) -> int:
        return self.arr[-1][0]
        

    def getMin(self) -> int:
        return self.arr[-1][1]

        
