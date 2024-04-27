class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        N = len(s)
        M = len(t)
        total = 0
        def go(i,j,can_skip):
            nonlocal total
            if can_skip == 0:
                total += 1
            if i == N or j == M:
                return
            if s[i] == t[j]:
                go(i+1,j+1,can_skip)
            else:
                if can_skip == 1:
                    go(i+1,j+1,0)
        
        for i in range(N):
            for j in range(M):
                go(i,j,1)
        return total