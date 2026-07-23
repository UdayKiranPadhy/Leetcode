from functools import cache

class Solution:
    def minimumDistance(self, word: str) -> int:

        def dist(a, b):
            if a == -1 or b == -1:
                return 0

            ax, ay = divmod(a, 6)
            bx, by = divmod(b, 6)

            return abs(ax - bx) + abs(ay - by)

        nums = [ord(c) - ord('A') for c in word]
        n = len(nums)

        @cache
        def go(index, left, right):
            if index == n:
                return 0

            ch = nums[index]

            # Use left finger
            use_left = dist(left, ch) + go(index + 1, ch, right)

            # Use right finger
            use_right = dist(right, ch) + go(index + 1, left, ch)

            return min(use_left, use_right)

        return go(0, -1, -1)