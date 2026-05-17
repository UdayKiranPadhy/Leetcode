class Solution:
    def profitableSchemes(self, n, minProfit, group, profit):

        MOD = 10**9 + 7
        N = len(group)

        from functools import cache

        @cache
        def go(i, membersLeft, profitNeeded):

            # all crimes considered
            if i == N:
                return 1 if profitNeeded == 0 else 0

            # skip current crime
            ans = go(i + 1, membersLeft, profitNeeded)

            # take current crime
            if membersLeft >= group[i]:

                newProfitNeeded = max(
                    0,
                    profitNeeded - profit[i]
                )

                ans += go(
                    i + 1,
                    membersLeft - group[i],
                    newProfitNeeded
                )

            return ans % MOD

        ans = go(0, n, minProfit)
        go.cache_clear()
        return ans