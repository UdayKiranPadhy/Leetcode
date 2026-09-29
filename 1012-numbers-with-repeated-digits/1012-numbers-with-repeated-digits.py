from functools import cache

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:

        N = len(str(n))
        n_digits = list(map(int, str(n)))

        @cache
        def go(pos, tight, started, mask):

            if pos == N:
                return 1 if started else 0

            limit = n_digits[pos] if tight else 9

            ans = 0

            # Don't start the number yet
            if not started:
                new_tight = tight and (0 == n_digits[pos])

                ans += go(
                    pos + 1,
                    new_tight,
                    False,
                    mask
                )

            # Choose an actual digit
            start_digit = 1 if not started else 0

            for next_digit in range(start_digit, limit + 1):

                # Digit already used -> duplicate
                if mask & (1 << next_digit):
                    continue

                new_mask = mask | (1 << next_digit)

                new_tight = (
                    tight and
                    next_digit == n_digits[pos]
                )

                ans += go(
                    pos + 1,
                    new_tight,
                    True,
                    new_mask
                )

            return ans

        # Count numbers WITHOUT repeated digits
        unique = go(0, True, False, 0)

        # Total positive numbers - unique-digit numbers
        return n - unique