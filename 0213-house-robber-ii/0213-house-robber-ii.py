class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        
        @cache
        def rob(index,rob1):
            if index >= N:
                return 0
            if index == 0:
                op1 = nums[index] + rob(index + 2, 1)
                op2 = rob(index+1,0)
                return max(op1,op2)
            elif index == N-1 and rob1==1:
                return rob(index+1,1)
            else:
                op1=nums[index]+rob(index + 2,rob1)
                op2=rob(index+1,rob1)
                return max(op1,op2)
            
        return rob(0,0)