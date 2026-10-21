class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        def dfs(i, j, wordIndex):
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != word[wordIndex]:
                return False
            elif board[i][j] == word[wordIndex] and wordIndex == len(word) - 1:
                return True
            board[i][j] = "#"
            for direction in directions:
                if dfs(i + direction[0], j + direction[1], wordIndex + 1):
                    return True
            board[i][j] = word[wordIndex]
            return False

        for i in range(n):
            for j in range (m):
                if dfs(i, j, 0):
                    return True

        return False
