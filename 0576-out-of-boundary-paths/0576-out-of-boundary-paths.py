class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def dfs(i,j,move):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 1
            if not move:
                return 0
            left = dfs(i-1,j,move-1)
            right = dfs(i+1,j,move-1)
            up = dfs(i,j-1,move-1)
            down = dfs(i,j+1,move-1)
            return left+right+up+down
        
        return dfs(startRow, startColumn, maxMove) % (10**9 + 7)