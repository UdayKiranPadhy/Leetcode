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
            return False
        if b > a:
            a , b = b ,a
        self.parent[b] = a
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        result = None
        dsu = DisJointsetUnion(len(edges))
        for u , v in edges:
            u , v = u -1 , v - 1
            if not dsu.union(u,v):
                result = [u+1,v+1]
                
        return result