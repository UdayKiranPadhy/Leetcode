class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)
        nums.insert(0,1)
        nums.append(1)

        @cache
        def go(i,j):
            if i > j:return 0
            maxi = -float('inf')
            for index in range(i,j+1):
                maxi = max(maxi, nums[i-1]*nums[index]*nums[j+1] + go(i,index-1) + go(index+1, j))
            return maxi


        return go(1,N)