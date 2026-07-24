from functools import cache

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        # Generate all valid row patterns
        patterns = []
        for a in range(3):
            for b in range(3):
                if a == b:
                    continue
                for c in range(3):
                    if b == c:
                        continue
                    patterns.append((a, b, c))

        # Build transition graph
        m = len(patterns)  # 12
        next_rows = [[] for _ in range(m)]

        for i in range(m):
            for j in range(m):
                ok = True
                for k in range(3):
                    if patterns[i][k] == patterns[j][k]:
                        ok = False
                        break
                if ok:
                    next_rows[i].append(j)

        @cache
        def dfs(row, prev):
            if row == n:
                return 1

            ans = 0

            if prev == -1:
                # First row
                for p in range(m):
                    ans = (ans + dfs(row + 1, p)) % MOD
            else:
                for nxt in next_rows[prev]:
                    ans = (ans + dfs(row + 1, nxt)) % MOD

            return ans

        return dfs(0, -1)