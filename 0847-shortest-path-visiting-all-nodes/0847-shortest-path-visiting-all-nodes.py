class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        # Multi Source BFS + Bit Masking

        N = len(graph)
        q = deque()

        for i in range(N):
            q.append([i,1<<i, 0])
        
        visited = set()

        while q:
            node , mask, steps = q.popleft()

            if mask == (1<<N) - 1:
                return steps
            
            for neibour in graph[node]:
                new_mask = mask | (1<<neibour)
                if (neibour, new_mask) not in visited:
                    visited.add((neibour,new_mask))
                    q.append([neibour, new_mask, steps + 1])

        return 0