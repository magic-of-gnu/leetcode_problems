class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = dict()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            return
        
        ind, a = self._containsWord(word)
        for char in word[ind:]:
            b = dict()
            a[char] = b
            a = b
            
        a[None] = None


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ind, d = self._containsWord(word)
        
        if ind == len(word):
            if None in d:
                return True
        
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        
        ind, _ = self._containsWord(prefix)
        if ind == len(prefix):
            return True
        
        return False
    
    def _containsWord(self, word):
        d = self.words
        for ind, char in enumerate(word):
            if char in d:
                d = d[char]
            else:
                return ind, d
            
        return ind+1, d
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
