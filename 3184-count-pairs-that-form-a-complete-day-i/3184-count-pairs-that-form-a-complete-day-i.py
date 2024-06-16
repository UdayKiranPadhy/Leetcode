class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        mapping = {}
        count = 0
        for hour in hours:
            remaining = hour % 24
            if (24 - remaining) % 24 in mapping :
                count += mapping[(24 - remaining) % 24]
            if remaining in mapping:
                mapping[remaining] += 1
            else:
                mapping[remaining] = 1
        return  count