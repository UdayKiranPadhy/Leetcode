"""
[3,0,6,1,5]
[0,1,3,5,6]

"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))