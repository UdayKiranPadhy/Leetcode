class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        perimeter = 0
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        def go(x,y):
            nonlocal perimeter
            grid[x][y] = 2
            for nx,ny in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
                perimeter += 1 if 0 > nx or nx >=R or 0> ny or ny >= C or grid[nx][ny] == 0  else 0

            for dx , dy in directions:
                nx , ny = x + dx , y + dy
                if 0<=nx<R and 0<=ny<C and grid[nx][ny] == 1:
                    go(nx,ny)
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    go(i,j)
        
        return perimeter