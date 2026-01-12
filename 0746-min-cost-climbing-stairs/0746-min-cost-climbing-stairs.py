class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)

        @cache
        def go(index):
            if index >= N:
                return 0
            return cost[index] + min( go(index+1) , go(index+2) )
        
        return min(go(0), go(1))