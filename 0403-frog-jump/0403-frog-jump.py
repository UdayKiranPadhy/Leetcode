class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        lastStone = stones[-1]
        available_stones = set(stones)

        @cache
        def go(stone, prev):
            if stone == lastStone:
                return True
            for jump in (prev - 1, prev, prev + 1):
                if jump <= 0:
                    continue
                nxt = stone + jump
                if nxt in available_stones:
                    if go(nxt, jump):
                        return True
            return False
        return go(0,0)