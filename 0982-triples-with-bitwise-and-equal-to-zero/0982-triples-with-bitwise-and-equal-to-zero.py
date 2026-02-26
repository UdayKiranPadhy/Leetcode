from collections import Counter

class Solution:
    def countTriplets(self, nums: list[int]) -> int:
        counts = Counter()
        for a in nums:
            for b in nums:
                counts[a & b] += 1
        res = 0
        for x in nums:
            for k, v in counts.items():
                if x & k == 0:
                    res += v
        return res