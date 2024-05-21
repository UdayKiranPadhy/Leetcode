class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N, ans = len(nums) , []
        
        def solve(index,subset):
            if index == N:
                ans.append(subset)
                return
            solve(index + 1, subset + [nums[index]])
            solve(index + 1, subset)
        
        solve(0,[])

        return ans