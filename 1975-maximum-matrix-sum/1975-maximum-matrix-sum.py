class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        minimum = float('inf')
        N= len(matrix)
        count = 0
        total = 0
        for i in range(N):
            for j in range(N):
                if matrix[i][j] < 0:
                    count += 1
                minimum = min(minimum,abs(matrix[i][j]))
                total += abs(matrix[i][j])

        if count%2 == 0:
            return total
        else:
            return total - 2*minimum