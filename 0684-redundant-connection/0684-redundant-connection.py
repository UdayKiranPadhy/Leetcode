class DisJointsetUnion:
    def __init__(self,n):
        self.parent = list(range(n))
    
    def find(self,a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy] , acopy = a , self.parent[acopy]
        return a 
    
    def union(self,u,v):
        a , b = self.find(u) , self.find(v)
        if a == b:
            return
        if b > a:
            a , b = b ,a
        self.parent[b] = a


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        result = None
        dsu = DisJointsetUnion(len(edges))
        for u , v in edges:

            u , v = u -1 , v - 1
            
            if dsu.find(u) == dsu.find(v):
                result = [u+1,v+1]
            else:
                dsu.union(u,v)
        return result