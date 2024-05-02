class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """
        2*i is the left 
        2*i + 1 is the right

        The left node has the value 2 * val, and
        The right node has the value 2 * val + 1.

        this means, no matter a node is left or right child,
        its parent is val / 2.

        For query x and y, we try to find their common ancestor.
        If x != y, we hadn't found yet.
        So we let the bigger node go up:
        if x > y, x = x / 2,
        if x < y, y = y / 2,
        and this take on step.
        We continue to do this until x == y.

        The cycle length is the number of steps plus 1.
        """
        result = []
        for x , y in queries:
            res = 1
            while x != y:
                if x > y:
                    x = x//2
                else:
                    y = y//2
                res += 1
            result.append(res)
        return result