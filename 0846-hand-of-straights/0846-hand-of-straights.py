class Solution:
    def isNStraightHand(self, nums: List[int], k: int) -> bool:
        available = {}
        for num in nums:
            if num in available:available[num]+=1
            else: available[num] = 1
        nums.sort()
        for num in nums:
            if num not in available:
                continue
            for i in range(k):
                if num + i not in available:
                    return False
            for i in range(k):
                available[num+i] -= 1
                if available[num+i] == 0:
                    del available[num+i]
        return True