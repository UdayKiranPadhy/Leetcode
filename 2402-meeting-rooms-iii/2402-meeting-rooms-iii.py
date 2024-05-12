class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available = list(range(n))
        busy = [] # (end_time, server_no)
        count = [0] * n

        points = meetings
        points.sort()

        for start, end in points:
            while busy and busy[0][0] <= start:
                _, index = heappop(busy)
                heappush(available, index)
            
            if not available:
                end_time, index = heappop(busy)
                dur = end - start
                start = end_time
                end = start + dur
                heappush(available, index)
            
            server = heappop(available)
            heappush(busy,[end, server])
            count[server] += 1

        return count.index(max(count))