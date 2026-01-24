class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l , r = 0 , len(nums)-1
        ans = -float('inf')
        while r > l:
            ans = max(ans, nums[r]+nums[l])
            l+=1
            r-=1
        return ans