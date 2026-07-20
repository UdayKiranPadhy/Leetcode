class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        
        @lru_cache(None)
        def go(sum):
            if sum == target:
                return 1
            ways = 0
            for i in range(len(nums)):
                if sum + nums[i] <= target:
                    ways += go(sum+nums[i])
            return ways

        return go(0)