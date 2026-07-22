class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        N = len(stations)
        dp = [startFuel] + [0] * N
        for i , (location, capacity) in enumerate(stations):
            for t in range(i,-1,-1):
                if dp[t] >= location:
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)
        
        for i, d in enumerate(dp):
            if d >= target:
                return i
        return -1