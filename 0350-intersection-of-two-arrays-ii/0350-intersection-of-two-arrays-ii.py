
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counter1, counter2 = Counter(nums1), Counter(nums2)
        counter = counter1 & counter2
        return list(counter.elements())