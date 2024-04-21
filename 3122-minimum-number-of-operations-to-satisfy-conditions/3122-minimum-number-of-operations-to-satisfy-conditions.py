class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        R , C = len(grid) , len(grid[0])
        freq = [Counter() for _ in range(C)]
        for c in range(C):
            for r in range(R):
                freq[c][grid[r][c]] += 1
        
        @cache
        def go(index, last):
            if index == C:
                return 0
            
            best = go(index+1,-1) + R
            for element , hz in freq[index].items():
                if element == last:
                    continue
                best = min(best , go(index+1, element) + R - hz)
            return best
        return go(0,-1)