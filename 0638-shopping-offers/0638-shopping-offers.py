class Solution:
    def shoppingOffers(self, price: List[int], specials: List[List[int]], needs: List[int]) -> int:

        @lru_cache(None)
        def dfs(needs):

            cost = sum(map(mul, needs, price))  # cost with no specials applied
            for special in specials:
                specPrice = special[-1]
                tmp = tuple(map(sub, needs, special[:-1]))  # reset need if special applied # pop() would make she special array shorter and shorter

                if min(tmp) < 0: continue  # special cannot be applied

                cost = min(cost, dfs(tmp)+ specPrice)  # id special best buy? # cost should be computed independently

            return cost  # return best cost for needs

        return dfs(tuple(needs))