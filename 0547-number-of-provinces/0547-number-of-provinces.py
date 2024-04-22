class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = set()
        comp = 0
        def dfs(node):
            if node in visited: return
            visited.add(node)
            for i in range(N):
                if isConnected[node][i] == 1: dfs(i)
            
        for i in range(N):
            if i not in visited:
                dfs(i)
                comp += 1
        return comp