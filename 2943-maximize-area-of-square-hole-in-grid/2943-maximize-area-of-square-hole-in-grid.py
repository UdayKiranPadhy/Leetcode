class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        h_intervals = []
        for bar in hBars:
            h_intervals.append([bar-1,bar+1])
        h_intervals.sort()
        
        v_intervals = []
        for bar in vBars:
            v_intervals.append([bar-1,bar+1])
        v_intervals.sort()
        
        print(h_intervals)
        print(v_intervals)

        # Merge Intervals
        new_h=[]
        for beg, end in h_intervals:
            if not new_h or new_h[-1][1] <= beg:
                new_h.append([beg,end])
            else:
                new_h[-1][1] = max(new_h[-1][1] , end)
        
        new_v=[]
        for beg, end in v_intervals:
            if not new_v or new_v[-1][1] <= beg:
                new_v.append([beg,end])
            else:
                new_v[-1][1] = max(new_v[-1][1] , end)
        
        print(new_h)
        print(new_v)
        
        # Count Distance
        max_h = 1
        for beg, end in new_h:
            max_h = max(max_h, end-beg)
        
        max_v = 1
        for beg, end in new_v:
            max_v = max(max_v, end-beg)
        
        l = min(max_v, max_h)
        return l**2