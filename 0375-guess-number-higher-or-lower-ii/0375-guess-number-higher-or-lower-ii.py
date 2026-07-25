class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        @cache
        def go(left, right):
            if left >= right:
                return 0
            
            ans = float('inf')
            for next in range(left,right+1):
                cost = next + max(go(left,next-1) , go(next+1,right))
                ans = min(ans, cost)
            return ans
        
        return go(1,n)