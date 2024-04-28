
class DisjointSetUnion:
    def __init__(self, N: int):
        self.parent = list(range(N))
        self.size = [1] * N
        self.comp = N

    def find(self, a: int) -> int:
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, u: int, v: int) -> None:
        a, b = self.find(u), self.find(v)
        if a == b:
            return
        if b > a:
            a, b = b, a
        self.size[a] += self.size[b]
        self.parent[b] = a
        self.comp -= 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        N = len(accounts)
        dsu = DisjointSetUnion(N)
        mappings = {}
        
        for idx , account in enumerate(accounts):
            name = account[0]
            for i in range(1,len(account)):
                email = account[i]
                if email in mappings:
                    parent = mappings[email]
                    dsu.union(parent,idx)
                mappings[email] = idx
        
        for key, value in mappings.items():
            mappings[key] = dsu.find(value)
        
        result = defaultdict(list)
        for key, value in mappings.items():
            result[value].append(key)
        
        final = []
        for key , value in result.items():
            name = accounts[key][0]
            merged = []
            merged.append(name)
            merged.extend(sorted(value))
            final.append(merged)
        return final