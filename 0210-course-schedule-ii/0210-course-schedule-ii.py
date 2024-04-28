class Solution:
    def findOrder(self, N: int, prerequisites: List[List[int]]) -> List[int]:
        cycle = False
        stack = []
        visited = [0] * N
        
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        def dfs(node):
            nonlocal cycle
            if cycle:
                return
            if visited[node] == 1:
                cycle = True
                return
            visited[node] = 1
            for next in graph[node]:
                if visited[next] != 2:
                    dfs(next)
            
            visited[node] = 2
            stack.append(node)

        for i in range(N):
            if cycle:
                break
            if visited[i] == 0:
                dfs(i)
        
        return [] if cycle else stack