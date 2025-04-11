class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low,high+1):
            if len(str(i))%2 != 0:
                continue
            number = str(i)
            half1 = number[:len(number)//2]
            half2 = number[len(number)//2:]
            sum1 , sum2 = 0,0
            for i in range(len(half1)):
                sum1 += int(half1[i])
            for i in range(len(half2)):
                sum2 += int(half2[i])
            if sum1 == sum2 :
                count += 1
        return count