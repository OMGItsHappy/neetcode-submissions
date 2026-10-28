class MedianFinder:

    def __init__(self):
        self.minHeap = [] # right
        self.maxHeap = [] # left
        
    def isEven():
        return (len(self.minHeap) + len(self.maxHeap)) // 2 == 0

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == 0 or num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        minLen, maxLen = len(self.minHeap), len(self.maxHeap)
        if minLen - maxLen > 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        if maxLen - minLen > 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return self.minHeap[0]
        
        