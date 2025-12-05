class Solution:
    def solveNQueens(self, n):
        def dfs(board, i, c1, c2, c3):
            if i == n: ans.append(["." * j + "Q" + "." * (n - j - 1) for j in board])

            for j in range(n):
                if c1 & 1 << j or c2 & 1 << i - j + n or c3 & 1 << i + j: continue
                dfs(board + [j], i + 1, c1 ^ 1 << j, c2 ^ 1 << i - j + n, c3 ^ 1 << i + j)

        ans = []
        dfs([], 0, 0, 0, 0)
        return ans