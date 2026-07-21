from functools import cache
from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:

        @cache
        def go(covered):
            if covered >= time:
                return 0

            ans = float('inf')

            for start, end in clips:
                if start <= covered < end:
                    ans = min(ans, 1 + go(end))

            return ans

        ans = go(0)
        return -1 if ans == float('inf') else ans