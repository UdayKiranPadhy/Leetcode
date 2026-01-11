class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        N , M = len(s1), len(s2)
        
        @cache
        def go(i,j):
            if i == N and j == M:
                return 0
            if i == N:
                return ord(s2[j]) + go(i,j+1)
            if j == M:
                return ord(s1[i]) + go(i+1,j)
            if s1[i] == s2[j]:
                return go(i+1,j+1)
            else:
                return min(ord(s1[i]) + go(i+1,j), ord(s2[j]) + go(i, j + 1) )
        
        return go(0,0)