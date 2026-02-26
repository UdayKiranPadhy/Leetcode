class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        water = [0] * (n+1)
        for i , r in enumerate(ranges):
            left = max(0 , i - r)
            right = min(n , i + r)
            water[left] = max(water[left], right)
        
        @cache
        def go(index):
            if index >= n:
                return 0
            
            min_taps = float('inf')

            for next_pos in range(water[index],index,-1):
                min_taps = min(min_taps , 1 + go(next_pos))
            return min_taps
        
        return go(0) if go(0) != float('inf') else -1