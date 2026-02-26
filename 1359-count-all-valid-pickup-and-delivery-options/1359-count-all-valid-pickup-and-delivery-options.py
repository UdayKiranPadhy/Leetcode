class Solution:
    def countOrders(self, n: int) -> int:
        @cache
        def totalOrders(unpicked,undelivered):
            if unpicked == 0 and undelivered == 0:
                return 1
            if unpicked < 0 or undelivered < 0 or unpicked > undelivered:
                return 0
            ans = unpicked * totalOrders(unpicked-1,undelivered)
            ans %= MOD
            
            ans += (undelivered - unpicked) * totalOrders(unpicked,undelivered - 1)
            ans %= MOD
            
            return ans
        
        MOD = 1000000007
        return totalOrders(n,n)