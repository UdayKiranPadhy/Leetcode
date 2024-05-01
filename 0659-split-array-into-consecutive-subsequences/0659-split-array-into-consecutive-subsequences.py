class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        available = {}
        vacancy = {}
        for num in nums:
            if num in available:
                available[num] += 1
            else:
                available[num] = 1
        for num in nums:
            if available[num] == 0:
                continue
            if num not in vacancy or not vacancy[num]:
                if num + 1 in available and available[num+1] and num + 2 in available and available[num+2]:
                    if num + 3 in vacancy:
                        vacancy[num+3] += 1
                    else:
                        vacancy[num+3] = 1
                    available[num] -=1
                    available[num+1] -= 1
                    available[num+2] -= 1
                else:
                    return False
            else:
                vacancy[num] -= 1
                if num + 1 in vacancy:
                    vacancy[num+1] += 1
                else:
                    vacancy[num+1] = 1
                available[num] -= 1
        
        if list(available.values()).count(0) == len(available.values()):
            return True
        return False