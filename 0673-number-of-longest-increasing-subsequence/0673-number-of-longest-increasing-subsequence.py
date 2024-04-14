class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        count = [1] * N

        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j]+1:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[i] == dp[j] +1:
                        count[i] += count[j]
        maxi = max(dp)
        ans = 0
        for i in range(N):
            if dp[i] == maxi: ans += count[i]
        return ans