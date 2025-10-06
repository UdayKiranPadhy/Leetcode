class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        N = len(grid)

        def valid(limit):
            seen = set()
            def dfs(x,y,limit):
                seen.add((x,y))
                if x == y == N - 1:
                    return
                for dx, dy in directions:
                    nx , ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and (nx,ny) not in seen and grid[nx][ny] <= limit:
                        dfs(nx,ny,limit)
            dfs(0,0,limit)
            return (N-1,N-1) in seen

        low, high = grid[0][0] , max(max(grid, key=max))
        while low < high:
            mid = (low + high)//2
            if mid >= grid[N-1][N-1] and valid(mid):
                high = mid
            else:
                low = mid + 1
        return high