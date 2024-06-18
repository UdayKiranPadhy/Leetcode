class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(profit, difficulty), reverse=True)
        worker.sort(reverse=True)
        total = 0
        job_pointer = 0
        for diff in worker:
            while job_pointer < len(jobs) and jobs[job_pointer][1] > diff:
                job_pointer += 1
            if job_pointer < len(jobs):
                total += jobs[job_pointer][0]

        return total