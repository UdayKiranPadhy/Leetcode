class Solution:
    def addOperators(self, s: str, target: int) -> List[str]:
        ans , N = [], len(s)
        def backtrack(index,path,curr, prev):
            if index == N:
                if curr == target:
                    ans.append(path)
                return
            for j in range(index,N):
                if j > index and s[index] == '0':break
                number = int(s[index:j+1])
                if index == 0:
                    backtrack(j+1,str(number),number,number)
                else:
                    backtrack(j+1, path + '+' + str(number), curr + number, number)
                    backtrack(j+1, path + '-' + str(number), curr - number, -number)
                    backtrack(j+1, path + '*' + str(number), curr-prev + prev*number, prev*number)
        
        backtrack(0,'',0,0)
        return ans