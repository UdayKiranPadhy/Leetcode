class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        N = len(ring)
        M = len(key)
        @cache
        def count(ringIndex, i):
            round = abs(i - ringIndex)
            warp = N - round
            return min(warp, round)
        
        @cache
        def solve(ringIndex, keyIndex):
            if keyIndex == M:
                return 0
            best = float('inf')
            for i in range(N):
                if ring[i] == key[keyIndex]:
                    steps = count(ringIndex, i) + 1 + solve(i , keyIndex + 1)
                    best = min(best, steps)
            return best
        
        return solve(0,0)