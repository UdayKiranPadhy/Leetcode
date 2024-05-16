class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        least_value = float('inf')

        for i in range(len(prices)):
            profit = max(profit, prices[i]- least_value)
            least_value = min(least_value , prices[i])
        
        return profit