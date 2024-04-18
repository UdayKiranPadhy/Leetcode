class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand , cnt = None , 0

        for i in nums:
            if cnt ==0 : cand = i
            cnt += 1 if cand == i else -1
        return cand