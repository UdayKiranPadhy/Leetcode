from functools import cache

class Solution:
    def maxStudents(self, seats: list[list[str]]) -> int:

        m = len(seats)
        n = len(seats[0])

        # Mask of seats that are available in each row
        available = []

        for r in range(m):
            mask = 0

            for c in range(n):
                if seats[r][c] == '.':
                    mask |= (1 << c)

            available.append(mask)

        # All masks that don't have adjacent students
        valid_masks = []

        for mask in range(1 << n):
            if mask & (mask << 1):
                continue

            valid_masks.append(mask)

        @cache
        def dp(row, prev_mask):
            """
            Maximum students we can place from `row`
            onwards, assuming the previous row has
            students represented by prev_mask.
            """

            if row == m:
                return 0

            ans = 0

            for curr_mask in valid_masks:

                # Cannot place student on broken seat
                if curr_mask & ~available[row]:
                    continue

                # Cannot sit diagonally to previous row
                if curr_mask & (prev_mask << 1):
                    continue

                if curr_mask & (prev_mask >> 1):
                    continue

                students = curr_mask.bit_count()

                ans = max(
                    ans,
                    students + dp(row + 1, curr_mask)
                )

            return ans

        return dp(0, 0)