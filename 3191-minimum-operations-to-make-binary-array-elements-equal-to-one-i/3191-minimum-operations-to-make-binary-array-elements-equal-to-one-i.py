class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        res = 0
        
        for i in range(len(nums)-2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i+1] = 1-nums[i+1] #Flips 1 to 0 and 0 to 1
                nums[i+2] = 1-nums[i+2] #Flips 1 to 0 and 0 to 1
                res += 1
        
        if nums[-1] == nums[-2] == nums[-3] == 1: # Edge case
            return res
        return -1
            