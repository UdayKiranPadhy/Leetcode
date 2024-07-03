class Solution:
    def minDifference(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 4:
            return 0
        nums.sort()

        # Kill 3 Biggest elements
        op1 = nums[N-4] - nums[0]

        # Kill 2 biggest elements 1 smallest element
        op2 = nums[N-3] - nums[1]

        # Kill 1 Biggest element 2 smallest elements
        op3 = nums[N-2] - nums[2]

        # Kill 3 smallest elements
        op4 = nums[N-1] - nums[3]

        return min(op1,op2,op3,op4)