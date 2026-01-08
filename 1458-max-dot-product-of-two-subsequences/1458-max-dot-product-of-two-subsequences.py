class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        N , M = len(nums1) , len(nums2)

        ans = -float('inf')

        @cache
        def go(i,j,taken):
            if i >= N or j >= M:
                if not taken:
                    return -float('inf')
                else:
                    return 0
            
            return max(
                go(i+1, j+1 , True) + nums1[i] * nums2[j],
                go(i+1,j,taken),
                go(i,j+1,taken)
            )
        
        return go(0,0,False)