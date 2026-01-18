
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        N= len(prices)

        @lru_cache(None)
        def profit(index,own,transatations):
            if index == N or transatations ==0:
                return 0
            
            if own==1:
                op1 = prices[index] + profit(index+1,0,transatations-1)
                op2 = profit(index+1,own,transatations)
                return max(op1,op2)
            else:
                op1 = -prices[index] + profit(index+1,1,transatations)
                op2 = profit(index+1,own,transatations)
                return max(op1,op2)
                
        
        if len(prices) < 2:
            return 0
        
        return profit(0,0,2)