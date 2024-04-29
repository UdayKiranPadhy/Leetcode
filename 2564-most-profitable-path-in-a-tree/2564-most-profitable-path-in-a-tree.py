class Solution:
    def find(self, node, parent=-1):
        if node == 0:
            self.path.append(0)
            return True
        for next in self.graph[node]:
            if next == parent:
                continue
            if self.find(next, node):
                self.path.append(node)
                return True
        return False

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        N = len(amount)
        self.graph = defaultdict(list)
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)

        self.path = []
        self.find(bob)
        bobs_path = self.path[::-1]

        mappings = {}
        for idx, value in enumerate(bobs_path):
            mappings[value] = idx

        def dfs(node, parent, time):
            best = float('-inf')
            cost = amount[node]
            if node in mappings and mappings[node] < time:
                cost = 0
            elif node in mappings and mappings[node] == time:
                cost = cost // 2

            if len(self.graph[node]) == 1 and parent != -1:
                return cost

            for next in self.graph[node]:
                if next == parent:
                    continue
                best = max(best, cost + dfs(next, node, time + 1))
            return best

        return dfs(0, -1, 0)