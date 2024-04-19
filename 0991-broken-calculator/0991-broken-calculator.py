class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ops = 0
        while target != startValue:
            if target > startValue and target%2 == 0:
                target //= 2
                ops += 1
            elif target > startValue and target%2 != 0:
                target += 1
                ops += 1
            elif startValue > target:
                ops += startValue - target
                break
        return ops