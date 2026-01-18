
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs)
        N = len(pairs)

        @cache
        def go(index, prev):
            if index == N:
                return 0

            c, d = pairs[index]
            a, b = prev

            op1 = -float('inf')

            # Can take into chain
            if b < c:
                # Take into chain
                op1 = 1 + go(index + 1, (c, d))

            # Dont take
            op2 = go(index + 1, prev)

            return max(op1, op2)

        return go(0, (-1002, -1001))