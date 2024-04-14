class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N = len(s)
        M = len(t)

        @cache
        def dp(i,j):
            if j == 0:
                return 1
            if i == 0 and j != 0:
                return 0
            if s[i-1] == t[j-1]:
                return dp(i-1,j-1) + dp(i-1,j)
            return dp(i-1,j)

        return dp(N,M)

model = Solution()
print(model.numDistinct("babgbag","bag"))