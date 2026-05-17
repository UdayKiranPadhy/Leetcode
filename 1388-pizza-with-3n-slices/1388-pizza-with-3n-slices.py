class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:

        picks = len(slices) // 3

        def solve(arr):

            N = len(arr)

            @lru_cache(None)
            def go(i, k):

                # picked enough
                if k == 0:
                    return 0

                # no elements left
                if i >= N:
                    return -float('inf')

                # pick current
                pick = arr[i] + go(i + 2, k - 1)

                # skip current
                skip = go(i + 1, k)

                return max(pick, skip)

            return go(0, picks)

        # break circular dependency
        return max(
            solve(slices[:-1]),   # exclude last
            solve(slices[1:])     # exclude first
        )