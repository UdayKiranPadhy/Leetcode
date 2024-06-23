class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mind = deque()
        maxd = deque()
        i = 0
        for num in nums:
            while mind and mind[-1] > num: mind.pop()
            while maxd and maxd[-1] < num: maxd.pop()
            mind.append(num)
            maxd.append(num)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == nums[i]: maxd.popleft()
                if mind[0] == nums[i]: mind.popleft()
                i += 1
        return len(nums) - i