class Solution:
    def canFinish(self, N: int, edges: List[List[int]]) -> bool:
        graph =defaultdict(list)
        for u , v in edges:
            graph[u].append(v)
        
        def dfs(node):
            visited.add(node)
            path_visited.add(node)
            result = True
            for next in graph[node]:
                if next in path_visited:
                    return False
                if next not in visited:
                    result &= dfs(next)
            path_visited.remove(node)
            return result

        visited = set()
        path_visited = set()
        for i in range(N):
            if i not in visited:
                if not dfs(i):
                    return False
        return True


