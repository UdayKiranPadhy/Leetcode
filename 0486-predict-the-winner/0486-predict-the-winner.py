class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        @cache
        def go(l, r):
            if l == r:
                return nums[l]
            
            take_left = nums[l] - go(l+1, r)
            take_right = nums[r] - go(l, r-1)
            return max(take_left, take_right)
        
        return go(0,len(nums)-1) >= 0