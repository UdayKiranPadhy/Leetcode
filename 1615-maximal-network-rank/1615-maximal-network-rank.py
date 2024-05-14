class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        """
    TC :- O(N^2) , but there is another approach with O(N + E) using degrees but since E its N^2
    SC :- O(N^2) N^2 Edges
        """
        graph = {i:[] for i in range(n)}
        for u , v in roads:
            graph[u].append(v)
            graph[v].append(u)

        result = 0
        for i in range(n-1):
            for j in range(i+1,n):
                result = max(result, len(graph[i]) + len(graph[j]) - (i in graph[j]) )
        return result