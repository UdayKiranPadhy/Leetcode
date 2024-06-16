class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, index, N, covered = 0 , 0 , len(nums), 1

        while covered <= n:
            if index < N and nums[index] <= covered:
                covered += nums[index]
                index += 1
            else:
                patches += 1
                covered += covered
        
        return patches