class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        freq = []
        for word in words:
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                if letter in word:
                    freq.append(word.count(letter))
                    break
        freq.sort()
        N = len(freq)
        result = []
        for query in queries:
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                if letter in query:
                    count = query.count(letter)
                    break
            result.append(N-bisect_right(freq,count))
        return result