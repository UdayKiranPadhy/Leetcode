class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        total, i = 0, 0
        N = len(nums)
        while i < N and i + 1 < N:
            if nums[i] + nums[i+1] == nums[0] + nums[1]:
                i+= 2
                total += 1
            else: break
        return total