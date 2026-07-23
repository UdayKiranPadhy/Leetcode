class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        index , days_left
        """
        N = len(jobDifficulty)

        @cache
        def go(index, days_left):
            if index == N and days_left:
                return float('inf')
            if index == N:
                return 0
            if days_left == 1:
                return max(jobDifficulty[index:N])
            
            maximum = float("-inf") 
            ans = float('inf')
            for i in range(index, N):
                maximum = max(maximum, jobDifficulty[i])
                ans = min(ans,maximum + go(i+1,days_left-1))
            
            return ans
        
        answer = go(0,d)
        if answer == float('inf'):
            return -1
        return answer