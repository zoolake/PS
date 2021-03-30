import collections
class TreeNode:
    def __init__(self):
        self.flag = False
        self.children = collections.defaultdict(TreeNode)

class Trie:
    def __init__(self):
        self.root = TreeNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.flag = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.flag
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True