class Solution:
    def longestArithSeqLength(self, A):
        best = Counter()
        for i in range(len(A)):
            for j in range(i):
                d = A[i] - A[j]
                best[(i,d)] = max(best[(i,d)], 1+best[(j,d)])
        return max(best.values()) + 1