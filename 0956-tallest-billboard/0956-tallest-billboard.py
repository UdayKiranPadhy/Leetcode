class Solution:
    def tallestBillboard(self, rods):

        from functools import cache

        n = len(rods)

        @cache
        def go(i, diff):

            if i == n:
                return 0 if diff == 0 else -float('inf')

            rod = rods[i]

            # ignore
            ans = go(i + 1, diff)

            # add to taller side
            ans = max(
                ans,
                go(i + 1, diff + rod)
            )

            # add to shorter side
            ans = max(
                ans,
                min(diff, rod) +
                go(i + 1, abs(diff - rod))
            )

            return ans

        return go(0, 0)