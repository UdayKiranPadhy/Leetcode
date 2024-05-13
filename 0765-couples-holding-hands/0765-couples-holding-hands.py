class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        swap, N = 0, len(row)

        mapping = {val : idx for idx , val in enumerate(row)}

        for i in range(N):
            element = row[i]

            if element %2 == 0: couple = element + 1
            else: couple = element - 1

            index_of_couple = mapping[couple]
            if abs(i-index_of_couple) > 1:
                mapping[couple] = i + 1
                mapping[row[i+1]] = index_of_couple
                row[i+1] , row[index_of_couple] = row[index_of_couple] , row[i+1]
                swap += 1
        return swap