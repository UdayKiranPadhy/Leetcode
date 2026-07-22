from functools import cache

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        N = len(nums)

        # Prefix sums for O(1) range sum queries
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i + 1] = prefix[i] + nums[i]

        @cache
        def go(index, moves):
            remaining = N - index

            # Impossible: not enough elements to form 'moves' non-empty partitions
            if remaining < moves:
                return float("inf")

            # Last partition must take everything
            if moves == 1:
                return prefix[N] - prefix[index]

            total = 0
            ans = float("inf")

            # Leave at least (moves-1) elements for the remaining partitions
            for j in range(index, N - moves + 1):
                total += nums[j]

                candidate = max(total, go(j + 1, moves - 1))
                ans = min(ans, candidate)

            return ans

        return go(0, k)