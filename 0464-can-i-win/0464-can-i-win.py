class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        # Already reached the target
        if desiredTotal <= 0:
            return True

        # Sum of all available numbers is not enough
        total = maxChoosableInteger * (maxChoosableInteger + 1) // 2

        if total < desiredTotal:
            return False
        
        @cache
        def go(mask, remaining):
            
            for i in range(1, maxChoosableInteger + 1):

                #Check if the we can take that integer
                if mask & (1<<i):
                    continue
                
                # Choosing i immeditely wins
                if i >= remaining:
                    return True
                
                # Choose i and give turn to opponent
                new_mask = mask | (1<<i)

                # If opponent cant win, we can win
                if not go(new_mask, remaining - i):
                    return True

            return False
        
        return go(0, desiredTotal)