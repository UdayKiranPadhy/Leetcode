class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        bits = 0
        for i in range(n):
            bits |= nums[i]
        ans = bits * pow(2, n-1)
        return ans