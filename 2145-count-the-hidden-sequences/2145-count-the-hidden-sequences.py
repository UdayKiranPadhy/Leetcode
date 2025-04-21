class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        low, high, total = 0,0, 0
        for diff in differences:
            total += diff
            low = min(total,low)
            high = max(total,high)
        
        height = abs(high) + abs(low)

        ans = 0
        while lower + height <= upper:
            ans += 1
            lower += 1
        
        return ans