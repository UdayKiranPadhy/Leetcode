class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.insert(0, 0)
        cuts.append(n)
        cuts.sort()
        @cache
        def go( i , j):
            if i > j: return 0
            mini = float('inf')
            for k in range(i,j+1):
                mini = min(mini , cuts[j+1] - cuts[i-1] + go(i , k-1) + go(k+1, j))
            return mini

        return go(1, len(cuts) - 2) 