class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @cache
        def dp(l, r):
            if l >= r:
                return piles[l]
            
            take_left = piles[l] - dp(l+1, r)
            take_right = piles[r] - dp(l, r-1)
            return max(take_left , take_right)
        
        return dp(0, len(piles) - 1) >= 0