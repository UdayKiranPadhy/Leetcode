class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        @cache
        def go(index):
            if index < 2:
                return 0
            
            if nums[index] - nums[index-1] == nums[index-1] - nums[index-2]:
                return 1 + go(index-1)
            
            return 0
        
        total = 0
        for i in range(len(nums)):
            total += go(i)
        
        return total