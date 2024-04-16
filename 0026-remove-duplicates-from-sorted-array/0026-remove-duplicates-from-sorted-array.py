class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        N = len(nums)
        for right in range(1,N):
            if nums[left] == nums[right]:
                continue
            left += 1
            nums[left] = nums[right]
        return left + 1