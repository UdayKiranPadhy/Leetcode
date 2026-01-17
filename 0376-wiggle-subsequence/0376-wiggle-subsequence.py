class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)

        @cache
        def go(index,prev,diff):
            if index == N:
                return 0
            if prev == -1:
                return max(1 + go(index+1,index,1), 1 + go(index+1,index,-1), go(index+1,prev,diff))
            if diff > 0 and nums[index] - nums[prev] > 0:
                return max(1+ go(index+1, index,-1) , go(index+1, prev,diff))
            if diff < 0 and nums[index] - nums[prev] < 0:
                return max(1 + go(index+1, index,1), go(index+1, prev, diff))
            return go(index+1,prev,diff)
        
        return go(0,-1,0)