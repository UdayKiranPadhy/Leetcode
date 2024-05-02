class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        res = 0
        for i in range(n//2-1 ,-1 ,-1):
            l , r = 2*i + 1, 2*i + 2
            res += abs(cost[l]- cost[r])
            cost[i] += max(cost[l],cost[r])
        return res