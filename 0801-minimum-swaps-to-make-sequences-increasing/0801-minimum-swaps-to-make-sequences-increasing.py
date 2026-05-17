class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)

        @cache
        def go(i,last_swap):
            if i == N:
                return 0
            
            prev1 = nums1[i-1]
            prev2 = nums2[i-1]

            if last_swap:
                prev1 , prev2 = prev2 , prev1
            
            ans = float('inf')

            if prev1 < nums1[i] and prev2 < nums2[i]:
                ans = go(i+1, False)
            
            if nums2[i] > prev1 and nums1[i] > prev2:
                ans = min(ans , 1 + go(i+1,True))
            
            return ans
        
        return min(go(1,False), 1 + go(1,True))