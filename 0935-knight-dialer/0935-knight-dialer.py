
class Solution:
    def knightDialer(self, N: int) -> int:
        from functools import lru_cache
        
        neighbours = {
            0:(4,6),
            1:(6,8),
            2:(7,9),
            3:(4,8),
            4:(0,3,9),
            5:(),
            6:(0,1,7),
            7:(2,6),
            8:(1,3),
            9:(2,4)
        }
        mod = 10**9 + 7
        @lru_cache(None)
        def dp(onKey, stepsLeft):
            if stepsLeft == 0:
                return 1
            elif stepsLeft == 1:
                return len(neighbours[onKey])
            else:
                tRes = 0
                for nextKey in neighbours[onKey]:
                    tRes += dp(nextKey, stepsLeft - 1)
                return tRes
                
        if N == 0: return 0
        else:
            res = 0
            for i in range(10):
                res += dp(i, N-1)
        return res % mod