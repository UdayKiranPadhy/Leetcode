class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        
        @cache
        def go(index,maximum,search_cost):
            if index == n:
                return 1 if search_cost == k else 0
            
            if search_cost > k:
                return 0
            
            total = 0
            
            # Pick something less than maximum
            if maximum > 0:
                total += maximum * go(index+1, maximum, search_cost)
            
            # Pick something greater than maximum
            for new_max in range(maximum+1, m + 1):
                total += go(index+1, new_max, search_cost + 1)
            
            return total % (10**9  + 7)
        
        return go(0,0,0)