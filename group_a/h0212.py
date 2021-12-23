class PrefixTree:
    def __init__(self, words):
        self.database = dict()
        
        [self.insert(word) for word in words]
        
    
    def insert(self, word):
        
        ind, d = self._search(word, self.database, 0)
        
        for char in word[ind:]:
            b = dict()
            d[char] = b
            d = b
            
        d[True] = True
        
    def _search(self, word, d, start_ind):
        
        for ind, char in enumerate(word):
            if char in d:
                d = d[char]
            else:
                return ind, d
            
        return ind+1, d
    
    def search_by_word_ind(self, word, d, ind):
        if word[ind] in d:
            return True, d[word[ind]]
        
        return False, d
    
        
    def search_by_char(self, char, d):
        if char in d:
            return True, d[char]
        
        return False, d
    
    def _remove_word(self, word):
        '''Assume word in database for sure'''
        
        def dfs(word, d, ind):
            
            if ind == len(word):
                if True in d and len(d) == 1:
                    return 2
                return 1
            
            if word[ind] not in d:
                return 0
            
            if word[ind] in d:
                is_found = dfs(word, d[word[ind]], ind+1)
            
            if is_found != 2:
                return is_found
            elif is_found == 2:
                d.pop(word[ind])
                if len(d) == 0:
                    return 2
                return 1

        dfs(word, self.database, 0)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        prefix_tree = PrefixTree(words)
        
        words = set(words)
        
        m, n = len(board), len(board[0])
        k = len(words)
        results = set()
                
        possible_letters = set(''.join(words))
        for ii in range(m):
            for jj in range(n):
                if board[ii][jj] not in possible_letters:
                    board[ii][jj] = "#"
        
        def dfs(board, d, ii, jj, word_path, results):
            
            if not (0 <= ii < m and 0 <= jj < n):
                return
            
            if board[ii][jj] == '#': # visited previously
                return
            
            char = board[ii][jj]
            
            is_found, newd = prefix_tree.search_by_char(char, d)
            
            if is_found is False:
                return
            
            if True in newd:
                word = word_path + char
                prefix_tree._remove_word(word)
                if word in words:
                    results.update([word])
            
            board[ii][jj] = '#'

            for di, dj in [(-1,0), (0,1), (1,0), (0,-1)]:
                x, y = ii + di, jj + dj
                dfs(board, newd, x, y, word_path+char, results)
                
            board[ii][jj] = char
            return
        
        for ii in range(m):
            for jj in range(n):
                dfs(board, prefix_tree.database, ii, jj, '', results)
        
        return list(results)
