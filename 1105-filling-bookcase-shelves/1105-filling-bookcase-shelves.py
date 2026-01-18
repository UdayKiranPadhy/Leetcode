class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        N = len(books)

        @cache
        def go(index, width_remaining,curr_height):
            if index == N:
                return 0
            op1 = float('inf')
            thickness , height = books[index]
            if width_remaining and thickness <= width_remaining:
                op1 = max(0,height - curr_height) + go(index+1,width_remaining - thickness, curr_height + max(0,height - curr_height))
            op2 = height + go(index+1, shelfWidth - thickness, height)
            return min(op1,op2)
        
        return go(0,shelfWidth, 0)