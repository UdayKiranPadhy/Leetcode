class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        R , C = len(board), len(board[0])
        comp = 0
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'X':
                    if i-1 >= 0 and board[i-1][j] =='X':
                        continue
                    if j-1 >= 0 and board[i][j-1] == 'X':
                        continue
                    comp += 1
        return comp