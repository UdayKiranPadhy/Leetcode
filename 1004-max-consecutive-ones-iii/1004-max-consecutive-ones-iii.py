class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        N = len(nums)
        left = 0
        best = 0
        flips = 0

        for right in range(N):
            if nums[right] == 0:
                flips += 1
            
            while flips > k:
                if nums[left] == 0:
                    flips -= 1
                left += 1
            
            best = max(best , right - left + 1)
        
        return best