class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N1 = len(nums1)
        N2 = len(nums2)
        if N1 > N2:
            return self.findMedianSortedArrays(nums2,nums1)
        N = N1 + N2
        low, high = 0 , N1
        left = (N1 + N2 + 1) // 2
        while low <= high:
            mid1 = (low + high)//2
            mid2 = left - mid1
            l1 = l2 = -float('inf')
            r1 = r2 = float('inf')
            if mid1 > 0: l1 = nums1[mid1-1]
            if mid2 > 0: l2 = nums2[mid2-1]
            if mid1 < N1: r1 = nums1[mid1]
            if mid2 < N2: r2 = nums2[mid2]
            if l1 <= r2 and l2 <= r1:
                if N % 2 == 1: return max(l1, l2)/1.0
                else: return (max(l1,l2) + min(r1,r2)) / 2.0
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1