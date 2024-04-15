
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

	# 1. Check states that would make a solution impossible
	#    i.  max(nums) is greater than target
	#    ii. sum(nums) is not evenly divisible by k
        total = 0
        maxi = float('-inf')
        for n in nums:
            total += n
            maxi = max(n, maxi)

        if total%k: return False
        target = total // k
        if maxi > target: return False

        # 2. Find all sets of numbers that add to target value
        #    i.  t = sum of numbers used i.e. nums[1]+nums[2]+nums[4]        4 21
        #    ii. p = bit-masked path     i.e. nums[1], nums[2], nums[4] = '0b10110'
        def bin_finder(i, t, p):
            nonlocal paths, nums

            if t == target:
                paths.append(p)
                return None

            if (t > target) or (i == len(nums)):
                return None

            bin_finder(i+1, t, p)
            bin_finder(i+1, t+nums[i], p|(1 << i))

        paths = []
        bin_finder(0, 0, 0)

        # 3. Every path in paths sums to the target value, find k paths that do not overlap
        #    i.e. for Example 1: nums = [4, 3, 2, 3, 5, 2, 1]
        #             paths = [[5],     [1,4],     [2,3],  [2,3]]
        #             paths = ['10000', '1000001', '1100', '100010'] when bitmasked using their indices
        #                        p1   |     p2     |  p3  |   p4  = '1111111'
        #             so every index was used (all ones) and each path sums to the target value
        target_path = (1 << len(nums)) - 1
        def path_finder(i, p):
            nonlocal res, paths

            if res: return None

            if p == target_path:
                res = True
                return None

            if i == len(paths):
                return None

            if not paths[i]&p:
                path_finder(i+1, p|paths[i])
            path_finder(i+1, p)

        res = False
        path_finder(0, 0)
        return res