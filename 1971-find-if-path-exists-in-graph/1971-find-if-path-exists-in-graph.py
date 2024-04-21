class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        edge = defaultdict(list)
        for a,b in edges:
            edge[a].append(b)
            edge[b].append(a)
        
        seen = set()
        def dfs(node):
            if node == destination:
                return True
            seen.add(node)
            for child in edge[node]:
                if child not in seen:
                    if dfs(child):
                        return True

        if dfs(source):
            return True
        return False