class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        A = [] # thieves
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    A.append([i, j])

        visited = [[0 for j in range(n)] for i in range(m)]
        distance = [[0 for j in range(n)] for i in range(m)]

        # find the minimum mahatten distance of each cell to theives 
        depth = 0
        while A:
            B = []
            for i, j in A:
                if not visited[i][j]:
                    visited[i][j] = 1
                    distance[i][j] = depth
                    for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                        if 0 <= x < m and 0 <= y < n:
                            B.append([x, y])
            A = B
            depth += 1
            
        # start from 0,0 and use dijkstra  
        visited = [[0 for j in range(n)] for i in range(m)]
        pq = [[-distance[0][0], 0, 0]]
        while pq:
            dis, i, j = heapq.heappop(pq)
            if visited[i][j]:
                continue
            visited[i][j] = 1
            if i == m - 1 and j == n - 1:
                return -dis

            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= x < m and 0 <= y < n:
                    heapq.heappush(pq, [-min(-dis, distance[x][y]), x, y])

        return -1