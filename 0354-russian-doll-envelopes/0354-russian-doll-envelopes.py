class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0],-x[1]))

        heights = [x[1] for x in envelopes]

        def LIS(nums):
            dp = []
            for i in nums:
                idx = bisect_left(dp,i)
                if idx == len(dp):
                    dp.append(i)
                else:
                    dp[idx] = i
            return len(dp)

        return LIS(heights)