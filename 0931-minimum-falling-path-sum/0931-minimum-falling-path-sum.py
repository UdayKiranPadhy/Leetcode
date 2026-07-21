class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        @cache
        def dfs(i,j):
            if j < 0 or j >= N:
                return float('inf')
            if i == N-1:
                return matrix[i][j]
            
            return matrix[i][j] + min(dfs(i+1,j), dfs(i+1, j-1), dfs(i+1,j+1))
        
        ans = float('inf')
        for i in range(N):
            ans = min(ans, dfs(0,i))
        return ans