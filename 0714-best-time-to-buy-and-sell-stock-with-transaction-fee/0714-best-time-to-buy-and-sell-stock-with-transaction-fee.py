class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        @cache
        def go(index,can_buy):
            if N == index:
                return 0
            
            op1 = 0
            if can_buy:
                op1 = -prices[index] + go(index+1, False)
            
            if not can_buy:
                op1 = prices[index] - fee + go(index+1,True)
            
            op2 = go(index+1,can_buy)

            return max(op1,op2)
        
        return go(0,True)