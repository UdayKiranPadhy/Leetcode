class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        
        def solve(row,used_columns,used_diagonals,used_diagonals2):
            if row == n:
                nonlocal ans
                ans +=1
                return
            for col in range(n):
                if col not in used_columns:
                    diag = row - col
                    diag2 = row + col
                    if diag not in used_diagonals and diag2 not in used_diagonals2:
                        used_columns.add(col)
                        used_diagonals.add(diag)
                        used_diagonals2.add(diag2)
                        
                        solve(row + 1,used_columns, used_diagonals,used_diagonals2)
                        
                        used_columns.remove(col)
                        used_diagonals.remove(diag)
                        used_diagonals2.remove(diag2)
                        
        solve(0,set(),set(),set())
        return ans