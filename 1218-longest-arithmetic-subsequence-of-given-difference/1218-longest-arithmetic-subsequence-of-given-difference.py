class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        indexes = defaultdict(list)
        for idx, value in enumerate(arr):
            indexes[value].append(idx)
        N = len(arr)

        @cache
        def go(idx):
            if idx == N:
                return 0
            next = arr[idx] + difference
            ans = 1
            next_index = bisect.bisect_left(indexes[next],idx+1)
            if next_index != len(indexes[next]):
                ans += go(indexes[next][next_index])
            return ans

        return max(go(i) for i in range(N))