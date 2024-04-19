class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        N = len(colors)
        maxPrev = time = 0
        for i in range(N):
            if i>0 and colors[i] != colors[i-1]:
                maxPrev = 0
            time += min(maxPrev, neededTime[i])
            maxPrev = max(maxPrev,neededTime[i])
        return time