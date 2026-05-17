class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        N = len(nums)

        @lru_cache(None)
        def go(index, target):
            if index == N and target == 0:
                return 1
            elif index == N and target != 0:
                return 0
            op1 = nums[index] + go(index + 1, target - nums[index])
            op2 = -nums[index] + go(index + 1, target + nums[index])
            return (op1+op2)

        return go(0, target)