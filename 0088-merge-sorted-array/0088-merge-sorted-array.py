class Solution:
    def merge(self, nums1, m, nums2, n):
        p1, p2 = m - 1, n - 1
        for i in range(m+n-1, -1, -1):
            if p1 < 0 or p2 < 0: break
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
              
        while p2 >= 0:
            nums1[i] = nums2[p2]
            i -= 1
            p2 -= 1