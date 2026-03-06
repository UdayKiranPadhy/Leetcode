class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)

        @cache
        def go(index,amount):
            if index >= N:
                return 0
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            take = go(index, amount - coins[index])
            skip = go(index + 1 , amount)
            return take + skip
        
        return go(0,amount)