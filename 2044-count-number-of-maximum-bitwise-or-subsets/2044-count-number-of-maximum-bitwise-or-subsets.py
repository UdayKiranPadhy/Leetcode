class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def subsets(L):
            res = [[]]
            for e in L:
                res += [sub + [e] for sub in res]
            return res
        subset = subsets(nums)
        def bor(l):
            res=0
            for i in l:
                res = res|i
            return res
        
        max_xor = 0
        for i in nums:
            max_xor |= i
        result = []
        for i in subset:
            if bor(i) == max_xor:
                result.append(i)
        return len(result)
            