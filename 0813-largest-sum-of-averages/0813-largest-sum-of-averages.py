class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        N = len(nums)

        @cache
        def go(index, moves):
            if index == N and moves:
                return -float('inf')
            if index == N:
                return 0
            total = 0
            ans = -float('inf')
            for j in range(index,N):
                total += nums[j]
                ans = max(ans, (total/(j-index+1)) + go(j+1, moves-1))
            return ans
        
        return go(0,k)