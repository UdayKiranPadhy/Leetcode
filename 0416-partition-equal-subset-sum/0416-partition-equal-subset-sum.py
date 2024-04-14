class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        @lru_cache(None)
        def KnapSack(index,sum):
            if sum == 0:
                return True
            elif index == 0 and sum !=0:
                return False
            elif nums[index-1] <= sum :
                return KnapSack(index-1,sum-nums[index-1]) or KnapSack(index-1,sum)
            else:
                return KnapSack(index-1,sum)
        
        if sum(nums)%2 == 0:
            return KnapSack(len(nums),int(sum(nums)/2))
        else:
            return False