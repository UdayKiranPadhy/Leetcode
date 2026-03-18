
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        R , C = len(grid), len(grid[0])
        dp = [[0 for _ in range(C+1)] for _ in range(R+1)]
        for i in range(1, R+1):
            for j in range(1, C+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + grid[i-1][j-1]
        count =0
        for i in range(1, R+1):
            for j in range(1, C+1):
                if dp[i][j] <= k:
                    count +=1
        return count