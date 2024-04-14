class Solution:
    def minimumDeleteSum(self, s1, s2):
        s1, s2 = [0] + [ord(i) for i in s1], [0] + [ord(i) for i in s2]
        n1, n2 = len(s1), len(s2)
        
        @lru_cache(None)
        def dp(i1, i2):
            if i1 == 0 and i2 == 0: return 0
            if i1 == 0: return dp(i1, i2-1) + s2[i2]
            if i2 == 0: return dp(i1-1, i2) + s1[i1]
            if s1[i1] == s2[i2]: return dp(i1-1, i2-1)
            return min(dp(i1-1, i2) + s1[i1], dp(i1, i2-1) + s2[i2])
        
        return dp(n1 - 1, n2 - 1)