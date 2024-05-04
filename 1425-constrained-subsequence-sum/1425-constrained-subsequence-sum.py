class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        queue = deque()
        ans = -float('inf')
        dp = [0]*N
        for idx, num in enumerate(nums):
            maximum = max(0, dp[queue[0]] if queue else 0)
            dp[idx] = nums[idx] + maximum
            ans = max(ans,dp[idx])
            while queue and dp[idx] >= dp[queue[-1]]:
                queue.pop()
            queue.append(idx)
            if idx - queue[0] + 1 > k:
                queue.popleft()
        print(dp)
        return ans