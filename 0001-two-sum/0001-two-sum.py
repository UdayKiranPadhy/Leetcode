class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = defaultdict(list)
        for ind, value in enumerate(nums):
            freq[value].append(ind)
        
        for key in freq.keys():
            if target - key in freq:
                if key == target-key and len(freq[key]) < 2:
                    continue
                elif key == target-key:
                    return [freq[key][0],freq[key][1]]
                return [freq[key][0],freq[target-key][0]]