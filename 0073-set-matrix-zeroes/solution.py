class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        total_rows = len(matrix)
        total_col = len(matrix[0])

        first_row_has_zero = False
        first_col_has_zero = False

        for r in range(total_rows):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break
            
        for c in range(total_col):
            if matrix[0][c] == 0:
                first_row_has_zero = True
                break
            
        for i in range(1, total_rows):
            for j in range(1, total_col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, total_rows):
            if matrix[i][0] == 0:
                for j in range(1, total_col):
                    matrix[i][j] = 0

        for j in range(1, total_col):
            if matrix[0][j] == 0:
                for i in range(1, total_rows):
                    matrix[i][j] = 0

        if first_row_has_zero:
            for c in range(0, total_col):
                matrix[0][c] = 0
        if first_col_has_zero:
            for r in range(0, total_rows):
                matrix[r][0] = 0
         
