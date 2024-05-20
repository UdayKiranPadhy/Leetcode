class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        
        ds = list(product((-1, 0, 1), repeat=2))
        ds.remove((0, 0))
        
        for i, j in product(range(m), range(n)):
            live = board[i][j] & 1
            neighbors = 0
            for di, dj in ds:
                if 0 <= i + di < m and 0 <= j + dj < n:
                    neighbors += board[i + di][j + dj] & 1
            if neighbors == 3 or (live and neighbors == 2):
                board[i][j] |= 2

        for i, j in product(range(m), range(n)):
            board[i][j] >>= 1