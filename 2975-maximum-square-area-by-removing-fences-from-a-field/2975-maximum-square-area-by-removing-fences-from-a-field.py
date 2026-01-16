class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences = [1] + hFences + [m]
        vFences = [1] + vFences + [n]
        hFences.sort()
        vFences.sort()

        # Calculate Distance Between the Rods
        hDist = set()
        N = len(hFences)
        for i in range(N):
            for j in range(i+1,N):
                hDist.add(hFences[j]-hFences[i])
        
        vDist = set()
        N = len(vFences)
        for i in range(N):
            for j in range(i+1,N):
                vDist.add(vFences[j]-vFences[i])
        
        common = hDist.intersection(vDist)
        if not common:
            return -1
        return max(common)**2 % (10**9 + 7)