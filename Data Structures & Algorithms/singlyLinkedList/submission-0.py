class LinkedList:
    
    def __init__(self):
        self.arr = []

    
    def get(self, index: int) -> int:
        try:
            return self.arr[index]
        except:
            return -1
        

    def insertHead(self, val: int) -> None:
        self.arr.insert(0, val)
        

    def insertTail(self, val: int) -> None:
        self.arr.append(val)
        

    def remove(self, index: int) -> bool:
        try:
            self.arr.pop(index)
            return True
        except:
            return False
        

    def getValues(self) -> List[int]:
        return self.arr
        
