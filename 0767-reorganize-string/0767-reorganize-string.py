class Solution:
    def reorganizeString(self, s: str) -> str:
        max_heap = []

        frequency = Counter(s)

        for char, freq in frequency.items():
            heapq.heappush(max_heap, (-freq, char))

        result = ""

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            if result and result[-1] == char:
                if not max_heap:
                    return ""
                freq2, char2 = heapq.heappop(max_heap)
                result += char2
                if freq2 + 1 < 0:
                    heapq.heappush(max_heap, (freq2 + 1, char2))
                heapq.heappush(max_heap, (freq, char))
            else:
                result += char
                if freq + 1 < 0:
                    heapq.heappush(max_heap, (freq + 1 , char))
        return result