class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        N = len(satisfaction)
        satisfaction.sort()
        @cache
        def go(i,count):
            if i == N:
                return 0
            
            # pick
            ans = satisfaction[i]*count + go(i+1, count+1)

            ans = max(ans , go(i+1,count))

            return ans
        
        return go(0,1)