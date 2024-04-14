class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums.sort()
        dp = [1] * N
        prev = [-1] * N
        for i in range(N):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] =  dp[j]+1
                        prev[i] = j
        maximum = -float('inf')
        index = -1
        ans =[]
        for i in range(N):
            if dp[i] > maximum:
                maximum = max(maximum,dp[i])
                index = i
        
        while index != -1:
            ans.append(nums[index])
            index = prev[index]
        return ans