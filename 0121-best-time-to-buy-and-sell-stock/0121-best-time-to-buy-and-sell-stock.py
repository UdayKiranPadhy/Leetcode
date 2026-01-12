class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        max_profit = 0

        def go(left, right):
            nonlocal max_profit
            if right >= N:
                return
            max_profit = max(max_profit, prices[right] - prices[left])
            if prices[left] > prices[right]:
                left = right
            go(left,right+1)
        
        go(0,1)
        return max_profit