class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])

        def isWithin(i1, i2):
            if (i1[0] <= i2[0] and i1[1] >= i2[1]):
                return i1
            
            if (i1[1] >= i2[0] and i1[1] <= i2[1]):
                return [min(i1[0], i2[0]), max(i2[1], i1[1])]
            return None

        i = 0
        while i < len(intervals) - 1:
            res = isWithin(intervals[i], intervals[i + 1])
            if res:
                intervals[i] = res
                intervals.pop(i + 1)
                i -= 1 # Stay in same place so we can check next interval
            i += 1

        return intervals
            