
class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0 or x == 1:
            return x

        low = 1
        high = x // 2 + 1

        while low < high:

            mid = (low + high) // 2
            square = mid * mid

            if square == x:
                return mid
            if square > x:
                high = mid
            else:
                low = mid + 1

        return low - 1