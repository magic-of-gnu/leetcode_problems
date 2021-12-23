class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.words = dict()
        

    def addWord(self, word: str) -> None:
        
        ind, d = self._search(word, self.words, 0)
        
        for char in word[ind:]:
            b = dict()
            d[char] = b
            d = b
            
        d[True] = True

    def search(self, word: str) -> bool:
                
        ind, d = self._search(word, self.words, 0)
        
        if ind == len(word):
            if True in d:
                return True
        
        return False
        
    def _search(self, word, d, start_ind):
        
        ind = 0
        # if ends on "."
        if len(word) == start_ind:
            return start_ind, d
        
        
        for ind, char in enumerate(word[start_ind:], start=start_ind):
            
            
            if char == '.':
                # pass through all possible combinations except None
                
                for k, v in d.items():

                    
                    
                    if k is True:
                        continue
                        
                    _ind, _d = self._search(word, v, ind+1)

                    if _ind == len(word) and True in _d:
                        return _ind, _d
                    
                return ind, d
            
            elif char != '.':
                
                if char in d:
                    d = d[char]
                else:
                    return ind, d
                
        return ind+1, d
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
