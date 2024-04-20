class Solution:
    def maximum69Number (self, num: int) -> int:
        for index, value in enumerate(str(num)):
            if value == '6':
                break
        return int(str(num)[:index] + '9' + str(num)[index+1:])