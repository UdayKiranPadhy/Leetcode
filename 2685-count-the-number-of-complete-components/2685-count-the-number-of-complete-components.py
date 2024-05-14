class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        
        
        adj=defaultdict(list)
        
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        
        def dfs(i):
            
            component.add(i)
            for child in adj[i]:
                if child not in visited:
                    visited.add(child)
                    dfs(child)
        
        
        ans=0
        visited=set()
        
        for i in range(n):
            if i not in visited:
                component=set()
                visited.add(i)
                dfs(i)
                if all(len(adj[node]) == len(component)-1 for node in component):
                    ans+=1
                    
        
        return ans