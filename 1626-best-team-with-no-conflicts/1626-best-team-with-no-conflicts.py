class Solution:
    def bestTeamScore(self, scores, ages):

        players = sorted(zip(ages, scores))
        n = len(players)

        from functools import cache

        @cache
        def go(i, prev):

            if i == n:
                return 0

            # skip
            ans = go(i + 1, prev)

            # take
            if prev == -1 or players[i][1] >= players[prev][1]:
                ans = max(
                    ans,
                    players[i][1] + go(i + 1, i)
                )

            return ans

        ans = go(0, -1)
        go.cache_clear()
        return ans