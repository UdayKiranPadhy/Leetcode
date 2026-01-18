class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        N = len(nums)
        
        @cache
        def go(index,mod):
            if index == N:
                if mod == 0:
                    return 0
                else:
                    return -float('inf')
            
            op1 = nums[index] + go(index+1, (mod + nums[index])%3 )
            op2 = go(index+1,mod)
            return max(op1,op2)
        
        return go(0,0)