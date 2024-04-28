class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        G = [set() for i in range(n)]
        for i, j in connections:
            G[i].add(j)
            G[j].add(i)
        
        seen = [0] * n

        def dfs(node):
            if seen[node] == 1:
                return 0
            seen[node] = 1
            for next in G[node]:
                dfs(next)
            return 1
        
        comps = 0
        for i in range(n):
            if seen[i] == 0:
                dfs(i)
                comps += 1
        
        return comps -1