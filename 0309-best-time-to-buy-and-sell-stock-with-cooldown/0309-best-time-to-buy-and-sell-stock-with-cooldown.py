class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        
        @cache
        def go(index, own , cooldown):
            if index >= N:
                return 0
            
            if cooldown == 1:
                return go(index+1,own, 0)

            if own == 1:
                # Sell
                op1 = prices[index] + go(index + 1, 0, 1)
                # Dont Sell , Just Continue
                op2 = go(index+1, 1, 0)
                return max(op1, op2)
            else:
                # We dont own any stocks
                # Buy 1
                op1 = -prices[index] + go(index+1,1,cooldown)
                # Dont buy , Just move on
                op2 = go(index+1,own,cooldown)
                return max(op1,op2)
        return go(0,0,0)