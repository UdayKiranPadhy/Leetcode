class Solution:
    def maximumDetonation(self, B):
        """
        Time complexity: O(N^3)
Building the graph takes O(N^2)time. The time complexity of a typical DFS is O(V+E) where V represents the number of nodes, and E represents the number of edges. More specifically, there are n nodes and n^2 edges in this problem. We need to perform n depth-first searches.
        """
        n, ans, G = len(B), 0, defaultdict(list)
        
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if B[i][2]**2 >= (B[i][0] - B[j][0])**2 + (B[i][1] - B[j][1])**2:
                    G[i] += [j]
        
        
        def dfs(node, visited):
            for child in G[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, visited)

        for i in range(n):
            visited = set([i])
            dfs(i, visited)
            ans = max(ans, len(visited))
                          
        return ans