class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        @cache
        def go(i, j, move):
            if i < 0 or j < 0 or i >= n or j >= n:
                return 0

            if move == 0:
                return 1
            if move:
                op1 = go(i+2, j-1, move-1)
                op2 = go(i+2, j+1, move-1)
                op3 = go(i-2, j+1, move-1)
                op4 = go(i-2, j-1, move-1)
                op5 = go(i-1, j+2, move-1)
                op6 = go(i+1, j+2, move-1)
                op7 = go(i+1, j-2, move-1)
                op8 = go(i-1, j-2, move-1)
                return (op1 + op2 + op3 + op4 + op5 + op6 + op7 + op8)/8
            return 1
        
        return go(row, column, k)