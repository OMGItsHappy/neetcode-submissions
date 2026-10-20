class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def shade(i, j):
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
                return
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            if board[i][j] == "O":
                board[i][j] = "#"
                for dr in directions:
                    shade(i + dr[0], j + dr[1])

        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == "O" and (i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1):
                    
                    shade(i, j)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"