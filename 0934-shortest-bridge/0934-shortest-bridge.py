class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        
        q = deque()
        seen = set()
        def dfs(x,y):
            seen.add((x,y))
            q.append([x,y,0])
            for dx, dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                nx = x + dx
                ny = y + dy
                if (nx,ny) not in seen and 0<= nx < N and 0<= ny < M and grid[nx][ny] == 1:
                    dfs(nx,ny)
        
        found = False
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1 and found == False:
                    dfs(i,j)
                    found = True
        
        while q:
            x, y ,steps = q.popleft()
            for dx, dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                nx = x + dx
                ny = y + dy
                if (nx,ny) not in seen and 0<= nx < N and 0<= ny < M:
                    if grid[nx][ny] == 1:
                        return steps
                    q.append([nx,ny,steps+1])
                    seen.add((nx,ny))

        return 0