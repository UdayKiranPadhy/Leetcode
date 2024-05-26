class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count = {}
        for num in nums2:
            count.setdefault(num*k,0)
            count[num*k] += 1
        result = 0
        for num in nums1:
            for i in range(1,int(num**0.5+1)):
                if num%i == 0:
                    div = num // i
                    if i in count:
                        result += count[i]
                    if div != i and div in count:
                        result += count[div]
        return result