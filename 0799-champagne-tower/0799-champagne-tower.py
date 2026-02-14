class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * k for k in range(1,102)]
        tower[0][0] = poured
        
        for r in range(query_row):
            for c in range(len(tower[r])):
                extra = (tower[r][c] - 1 )/2
                if extra >0:
                    tower[r+1][c] += extra
                    tower[r+1][c+1] += extra
                
            
            
        return min(1,tower[query_row][query_glass])