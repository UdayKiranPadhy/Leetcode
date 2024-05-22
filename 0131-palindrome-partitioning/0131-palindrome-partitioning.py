class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalin(s,i,j):
            if i >= j:
                return True
            elif s[i]==s[j]:
                return isPalin(s,i+1,j-1)
            else:
                return False
        res = []
        part = []
        
        def dfs(i):
            if i >= len(s):
                res.append(part[:])
            for j in range(i,len(s)):
                if isPalin(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
                    
        dfs(0)
        return res
    
    