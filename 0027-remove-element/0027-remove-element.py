class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left , right, N = 0, 0, len(nums)

        for right in range(N):
            if nums[right] == val:
                continue
            nums[left] = nums[right]
            left += 1
        return left 