class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf: int) -> int:
        N = len(books)

        @cache
        def go(index, prev, height):
            if index == N:
                return 0

            op1 = float('inf')

            if prev + books[index][0] <= shelf:
                diff = books[index][1] - height
                if diff >= 0:
                    op1 = diff + go(index + 1, prev + books[index][0], books[index][1])
                else:
                    op1 = go(index + 1, prev + books[index][0], height)
            op2 = books[index][1] + go(index + 1, books[index][0], books[index][1])

            return min(op1, op2)

        return go(0, 0, 0)
