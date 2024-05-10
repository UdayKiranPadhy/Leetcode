class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        N = len(arr)
        result = []
        for i in range(N):
            for j in range(i,N):
                result.append([arr[i]/arr[j], arr[i],arr[j]])
        result.sort()
        return result[k-1][1:]