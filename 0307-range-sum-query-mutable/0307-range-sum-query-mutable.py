class BIT:

    def __init__(self,N):
        self.stree = [0] * (N + 1)

    def increase(self, idx, value):
        while idx < len(self.stree):
            self.stree[idx] += value
            idx |= idx + 1
    
    def sum(self,right):
        total = 0
        while right > 0:
            total += self.stree[right]
            right &= (right + 1)
            right -= 1
        return total

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bit = BIT(len(nums))
        for idx, value in enumerate(self.nums):
            self.bit.increase(idx,value)

    def update(self, index: int, val: int) -> None:
        self.bit.increase(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        if left != 0:
            return self.bit.sum(right+1) - self.bit.sum(left)
        return self.bit.sum(right+1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)