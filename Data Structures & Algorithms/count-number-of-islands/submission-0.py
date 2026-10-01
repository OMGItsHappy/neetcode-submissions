class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(x, y, grid):
            queue = [(x, y)]
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            def inBounds(pts):
                x, y = pts
                return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

            while queue:
                for i in range(len(queue)):
                    x, y = queue.pop(0)
                    if inBounds((x, y)) and grid[x][y] == "1":
                        grid[x][y] = "x"
                        for direction in directions:
                            dX, dY = direction
                            queue.append((x + dX, y + dY))

        total = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    bfs(row, col, grid)
                    total += 1

        return total
