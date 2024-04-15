class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def bisect_left(nums,target):
            left = 0
            right = len(nums)

            while left < right:
                mid = (left + right)//2

                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def bisect_right(nums,target):
            left = 0
            right = len(nums)

            while left < right:
                mid = (left + right)//2

                if target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            return left
        idx = bisect_left(nums,target)
        if idx < len(nums) and nums[bisect_left(nums,target)] == target:
            return [bisect_left(nums,target), bisect_right(nums,target)-1]
        return [-1,-1]