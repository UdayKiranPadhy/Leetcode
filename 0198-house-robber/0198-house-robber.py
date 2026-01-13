class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        @cache
        def go(index):
            if index >= N:
                return 0
            take = nums[index] + go(index+2)
            no_take = go(index+1)
            return max(take,no_take)
        return go(0)