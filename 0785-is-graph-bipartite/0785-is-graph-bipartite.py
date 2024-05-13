class Solution:
    def isBipartite(self, gr: List[List[int]]) -> bool:
        n = len(gr)
        # 0 represent no color yet, 1 and -1 represent 2 different colors
        colors = [0] * n

        # Need a for loop to start bfs from each vertex
        # To make sure we don't miss any disconnected vertices
        for vertex in range(n):

            # If a vertex is colored, it is already reached from another vertex
            # no need to do it again
            if colors[vertex] != 0: continue

            # If a vertext is not yet colored, assign color starting from that vertex
            # and expand using bfs/queue
            q = deque()
            q.append(vertex)
            colors[vertex] = 1

            while q:
                # Pop next vertex
                cur_v = q.popleft()

                for adj_v in gr[cur_v]:
                    # Assign color to adj (opposite color to curr) and add adj to queue
                    if colors[adj_v] == 0:
                        colors[adj_v] = -colors[cur_v]
                        q.append(adj_v)
                    # Return false if curr and adj has the same color 
                    elif colors[adj_v] == colors[cur_v]:
                        return False

        # If all vertices can be organized with 
        return True