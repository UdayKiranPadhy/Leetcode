class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        for i in range(len(matrix[0])):
            t = []
            for j in range(len(matrix)):
                t.append(matrix[j][i])
                print(matrix[j][i],end= " ")
            transpose.append(t)
        return transpose