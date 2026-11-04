class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = max(piles)
        mn = 1
        def calcTime(k):
            time = 0
            for pile in piles:
                time += math.ceil(pile/k)
            return time
        lastValidTime = mx
        while mn <= mx:
            mid = mn + ((mx-mn) // 2)
            time = calcTime(mid)
            if time > h:
                mn = mid + 1
            if time <= h:
                lastValidTime = min(mid, lastValidTime)
                mx = mid - 1
        return lastValidTime
