class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        low, high = 0, rows*cols-1

        while low <= high:
            mid = low + (high-low) // 2
            row = mid//cols
            col = mid%cols
            point = matrix[row][col]

            if point == target:
                return True

            elif point < target:
                low = mid + 1

            else:
                high = mid -1

        return False