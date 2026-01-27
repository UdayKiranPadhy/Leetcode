class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))

        cache = {}

        def dfs(i):
            if i == len(startTime):
                return 0

            if i in cache:
                return cache[i]

            # not including
            res = dfs(i + 1)

            # including

            # finding the next interval in O(n) in this approach
            # j = i + 1
            # while j < len(startTime):
            #     if jobs[j][0] >= jobs[i][1]:
            #         break
            #     j += 1
            

            # using binary search to find the next j using bisect module 
            # startTime should be >= jobs[i][1]
            j = bisect.bisect(jobs, (jobs[i][1], -1, -1))

            cache[i] = res = max(res, dfs(j) + jobs[i][2])
            return res
        
        return dfs(0)
         