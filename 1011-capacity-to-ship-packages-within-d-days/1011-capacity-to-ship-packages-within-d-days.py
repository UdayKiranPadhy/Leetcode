class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        N = len(weights)
        # 15
        # [1,2,3,4,5,6,7,8,9,10] 5
        def good(cap):
            day = 0
            index = 0
            total = 0
            while day < days and index < N:
                if total + weights[index] <= cap:
                    total += weights[index]
                    index += 1
                else:
                    day += 1
                    total = 0
            if index == N:
                return True
            return False
                
        
        low = min(weights)
        high = sum(weights)
        while low < high:
            mid = (low + high) // 2
            if good(mid):
                high = mid
            else:
                low = mid + 1
        return low