class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)

        @cache
        def go(total):
            if total > amount:
                return float('inf')
            if total == amount:
                return 0
            ans = float('inf')
            for coin in coins:
                ans = min(ans ,1 + go(total + coin))
            return ans
        
        return go(0) if go(0) != float('inf') else -1