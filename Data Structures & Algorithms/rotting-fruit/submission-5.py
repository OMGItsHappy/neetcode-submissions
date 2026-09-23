class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        level = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        freshTotal = 0

        for col in range(len(grid)):
            for row in range(len(grid[0])):
                if grid[col][row] == 2:
                    for y, x in directions:
                        if col + y > -1 and col + y < len(grid) and row + x > -1 and row + x < len(grid[0]) and grid[col + y][row + x] == 1:
                            queue.append((col + y, row + x))
                    grid[col][row] = -1
                freshTotal += grid[col][row] == 1

        rottedTotal = 0
        while queue:
            converted = False
            tmpQueue = []
            for col, row in queue:
                if grid[col][row] == 1:
                    converted = True
                    rottedTotal += 1
                    grid[col][row] = -1
                    for y, x in directions:
                        if col + y > -1 and col + y < len(grid) and row + x > -1 and row + x < len(grid[0]) and grid[col + y][row + x] == 1:
                            tmpQueue.append((col + y, row + x))
            level += converted
            queue = tmpQueue

        return level if rottedTotal == freshTotal else -1