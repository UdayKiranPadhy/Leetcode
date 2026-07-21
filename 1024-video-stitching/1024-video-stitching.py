class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        N = len(clips)

        @cache
        def go(index,covered):
            if covered >= time:
                return 0
            if index == N:
                return float('inf')
            
            ans = float('inf')
            for j in range(index,N):
                start , end = clips[j]
                if end > covered and start <= covered:
                    ans = min(ans , 1 + go(j+1,end))
            return ans
        
        gg = go(0,0)
        if gg == float('inf'):
            return -1
        return gg