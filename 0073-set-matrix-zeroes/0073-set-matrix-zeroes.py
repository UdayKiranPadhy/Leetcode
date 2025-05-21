class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_mask = 0
        column_mask = 0
        R , C = len(matrix), len(matrix[0])
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    row_mask |= (1<<i)
                    column_mask |= (1<<j)
        
        for i in range(R):
            for j in range(C):
                if row_mask & (1 << i):
                    matrix[i][j] = 0
                if column_mask & (1 << j):
                    matrix[i][j] =0