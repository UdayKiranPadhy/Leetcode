class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # 1. Initialize the heap
        heap = []
        for h in happiness:
            heapq.heappush(heap, -h)

        # 2. Pop the heap k times and add the happiness to the result
        result = 0
        for _ in range(k):
            h = -heapq.heappop(heap)
            to_add = h - _
            if to_add > 0:
                result += to_add

        return result
