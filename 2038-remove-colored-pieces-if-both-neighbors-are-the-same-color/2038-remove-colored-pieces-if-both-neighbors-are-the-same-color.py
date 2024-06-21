class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice , bob , N = 0, 0, len(colors)
        for i in range(1,N-1):
            if colors[i-1] == colors[i] == colors[i+1] == 'A':
                alice += 1
            if colors[i-1] == colors[i] == colors[i+1] == 'B':
                bob += 1
        return alice > bob