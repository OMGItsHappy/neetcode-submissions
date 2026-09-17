class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        def isEdge(row, col):
            return row < 0 or row >= m or col < 0 or col >= n

        def addPath(row, col):
            if row == m-1 and col == n-1:
                return 1
            if isEdge(row, col):
                return 0

            if dp[row][col] != -1:
                return dp[row][col]

            dp[row][col] = addPath(row + 1, col) + addPath(row, col + 1)
            return dp[row][col]

        return addPath(0, 0)