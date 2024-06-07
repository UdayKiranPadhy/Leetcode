class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):  # None
        node = self.root
        for symbol in word:
            node = node.children.setdefault(symbol, TrieNode())
        node.end_word = word

    def find(self, word):
        node = self.root
        for l in word:
            if l not in node.children or node.end_word:
                break
            node = node.children[l]
        return node.end_word if node.end_word else word


class Solution:
    def replaceWords(self, dictionary, sentence):
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        return " ".join(trie.find(word) for word in sentence.split())