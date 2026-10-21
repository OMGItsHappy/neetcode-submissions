class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, wordIndex):
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[wordIndex]:
                return False
            elif board[i][j] == word[wordIndex] and wordIndex == len(word) - 1:
                return True
            board[i][j] = "#"
            for direction in directions:
                if dfs(i + direction[0], j + direction[1], wordIndex + 1):
                    return True
            board[i][j] = word[wordIndex]
            return False

        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if dfs(i, j, 0):
                    return True

        return False
