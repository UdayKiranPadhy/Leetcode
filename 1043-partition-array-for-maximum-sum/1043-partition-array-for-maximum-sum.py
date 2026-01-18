class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)

        @cache
        def go(index):
            if index == N:
                return 0
            
            total = 0
            maxi = -1
            segment_len = 0
            for i in range(index, min(index+k,N)):
                segment_len += 1
                maxi = max(maxi , arr[i])
                total = max(total,(maxi * segment_len) + go(i + 1))
            return total
        
        return go(0)