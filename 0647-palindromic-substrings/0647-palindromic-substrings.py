class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)

        @cache
        def go(l, r):
            if l >= r:
                return True
            
            if s[l] != s[r]:
                return False
            
            return go(l+1, r-1)
        
        total = 0

        for i in range(N):
            for j in range(i,N):
                if go(i, j):
                    total += 1
        
        return total