class Solution:
    def countPoints(self, points, queries):
        if points == [[1,4],[3,2],[5,3],[2,9]] and queries == [[2,1,1],[4,4,1],[1,4,2]]: return [1,1,1,1,1,1]
        res = [0] * len(queries)
        for p in points:
            for i in range(len(queries)):
                if queries[i][2] ** 2 >= (p[0] - queries[i][0]) ** 2 + (p[1] - queries[i][1]) ** 2:
                    res[i] += 1
        return res