class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        N = len(nums)
        left = 0
        res = 0
        freq = Counter()

        for right in range(N):
            freq[nums[right]] += 1

            if freq[nums[right]] > k:
                while freq[nums[right]] > k:
                    freq[nums[left]] -= 1
                    left += 1
            
            res = max(res , right - left +1)
        
        return res