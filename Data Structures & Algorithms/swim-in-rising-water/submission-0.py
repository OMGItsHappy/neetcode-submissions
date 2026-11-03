class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        size = len(grid)
        visited = set()
        queue = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        visited.add((0, 0))
        while queue:
            t, i, j = heapq.heappop(queue)
            if i == size - 1 and j == size - 1:
                return t
            for di, dj in directions:
                newI, newJ = i + di, j + dj
                if newI < 0 or newJ < 0 or newI == size or newJ == size or (newI, newJ) in visited:
                    continue
                visited.add((newI, newJ))
                heapq.heappush(queue, [max(t, grid[newI][newJ]), newI, newJ])