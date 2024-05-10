class Solution:
    def searchMatrix(self, matrix, target):
        """
        What we have in this problem is matrix, which is sorted and what we use to find element in sorted structure? Correct, this is binary search. Imagine, that we have matrix

10 11 12 13 14 15 16 17 18 19 20 21

Let us flatten this matrix, so now we have 10 11 12 13 14 15 16 17 18 19 20 21 and do binary search in this list. However if you do it, we will have O(mn) complexity, so we will use virtual flatten: we do not do it for all matrix, but only for elements we need: if we need element number i from our flattened list, it coresponds to element matrix[i//m][i%m] in our matrix.

Complexity: time complexity is O(log mn), space complexity is O(1).


        """
        if not matrix or not matrix[0]: return False
        m, n = len(matrix[0]), len(matrix)
        beg, end = 0, m*n - 1
        while beg < end:
            mid = (beg + end)//2
            if matrix[mid//m][mid%m] < target:
                beg = mid + 1
            else:
                end = mid
        return matrix[beg//m][beg%m] == target