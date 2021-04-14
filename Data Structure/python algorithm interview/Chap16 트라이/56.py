import collections
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node.children[char]
            node = node.children[char]
        node.word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

    def startWith(self, prefix):
        node = self.node
        for char in prefix: 
            if char not in node.children:
                return False
            node = node.children[char]

        return True