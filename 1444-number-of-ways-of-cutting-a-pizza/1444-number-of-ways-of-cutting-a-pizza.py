from functools import cache

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        N = len(pizza)
        M = len(pizza[0])
        MOD = 10 ** 9 + 7

        # Does rectangle (r1,c1) -> (r2,c2) contain an apple?
        def check(r1, c1, r2, c2):
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if pizza[i][j] == 'A':
                        return True
            return False

        @cache
        def go(i, j, cuts):
            if cuts == k - 1:
                return 1 if check(i, j, N - 1, M - 1) else 0

            ans = 0

            # Horizontal cuts
            for r in range(i + 1, N):
                # Upper piece must contain an apple
                if check(i, j, r - 1, M - 1):
                    ans += go(r, j, cuts + 1)

            # Vertical cuts
            for c in range(j + 1, M):
                # Left piece must contain an apple
                if check(i, j, N - 1, c - 1):
                    ans += go(i, c, cuts + 1)

            return ans % MOD

        return go(0, 0, 0)