class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # Solution Explanation :- https://leetcode.com/problems/count-subarrays-with-fixed-bounds/solutions/4949181/98-43-easy-solution-with-explanation/
        res = 0
        left_idx = right_idx = bad_idx = -1

        for idx, num in enumerate(nums):
            if not minK <= num <= maxK:
                bad_idx = idx
            if minK == num:
                left_idx = idx
            if maxK == num:
                right_idx = idx
            
            res += max(0,min(left_idx,right_idx) - bad_idx)
        
        return res