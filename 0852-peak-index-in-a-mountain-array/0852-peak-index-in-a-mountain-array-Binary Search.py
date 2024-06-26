class Solution:
    def peakIndexInMountainArray(self, A):
        l, r = 0, len(A) - 1
        while l < r:
            m = (l + r) / 2
            if A[m] < A[m + 1]:
                l = m + 1
            else:
                r = m
        return l
