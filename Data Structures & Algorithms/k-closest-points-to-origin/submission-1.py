class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean = lambda x: (math.sqrt(x[0] ** 2 + x[1] ** 2), x)
        points = list(map(euclidean, points))
        heapq.heapify(points)
        res = []

        for point in range(k):
            res.append(heapq.heappop(points)[1])
        return res
