class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def try_all_combinations(i, sum):
            if i == len(nums):
                return sum == target
            return try_all_combinations(
                        i + 1,
                        sum + nums[i]
                    ) + try_all_combinations(
                        i + 1,
                        sum - nums[i]
                    )

        return try_all_combinations(0, 0)