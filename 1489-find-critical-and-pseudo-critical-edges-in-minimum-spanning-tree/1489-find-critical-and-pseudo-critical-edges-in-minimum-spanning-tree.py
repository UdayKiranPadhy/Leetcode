class Solution:
    def findCriticalAndPseudoCriticalEdges(self, N: int, edges: List[List[int]]) -> List[List[int]]:
        # edge = u , v ,w
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append([v,w])
            graph[v].append([u,w])
        
        def mst(init= None, exclude=None):
            marked = [False] * N
            ans = 0
            pq = [] # min heap 

            def visit(u):
                marked[u] = True
                for v , w in graph.get(u, []):
                    if exclude and u in exclude and v in exclude: continue
                    else: heappush(pq,[w,u,v])
            
            if init is not None:
                u , v , w = init
                ans += w
                visit(u) or visit(v)
            else:
                visit(0)
            while pq:
                w , u , v = heappop(pq)
                if marked[u] and marked[v] :continue
                ans += w
                if not marked[u]: visit(u)
                if not marked[v]: visit(v)
            return ans if all(marked) else float('inf')

        critical , pseudo = [] , []
        ref = mst()
        for idx , edge in enumerate(edges):
            if mst(exclude=edge[:2]) > ref: critical.append(idx)
            elif mst(init=edge) == ref: pseudo.append(idx)
        return [critical,pseudo]