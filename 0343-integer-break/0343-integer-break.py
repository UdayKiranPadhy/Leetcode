class Solution:
    def integerBreak(self, n: int) -> int:
        
        @cache
        def go(n):
            if n == 0 or n == 1:
                return 1

            ans = 0
            for i in range(1,n):
                ans = max(ans,i*go(n-i),i*(n-i))
            return ans
        
        return go(n)