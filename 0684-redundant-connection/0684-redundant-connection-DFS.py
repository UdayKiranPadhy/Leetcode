class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target: return True
                return any(dfs(nei, target) for nei in graph[source])
        
        for u , v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u,v):
                return u,v 
            graph[u].append(v)
            graph[v].append(u)