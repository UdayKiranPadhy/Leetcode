class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = 0
        length = 0  # number of bits needed for the current number
        MOD = 10**9 + 7
        for i in range(1, n + 1):
            if (i & (i - 1)) == 0:
                length += 1
            result = ((result << length) | i) % MOD
        return result

        