from heapq import heappop, heappush


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        pq = [1]
        seen = set([1])

        while len(pq):
            popedElement = heappop(pq)
            n -= 1
            if n == 0:
                return popedElement
            if popedElement*2 not in seen:
                seen.add(popedElement*2)
                heappush(pq, popedElement*2)
            if popedElement*3 not in seen:
                seen.add(popedElement*3)
                heappush(pq, popedElement*3)
            if popedElement*5 not in seen:
                seen.add(popedElement*5)
                heappush(pq, popedElement*5)
