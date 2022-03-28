from collections import defaultdict
from pprint import pprint as pp

class Solution:
    def longestWord(self, words):

        def update_graph(graph, char, ind, next_char):
            if char in graph and ind in graph[char]: # a in graph
                graph[char][ind].add(next_char)
            elif char in graph and ind not in graph[char]:
                graph[char][ind] = set([next_char])
            elif char not in graph:
                graph[char] = {ind: set([next_char])} # {a: {0:None}} {a: {0, None}, b: {0: {a}}}

        def update_answer(word, answer):
            if len(word) > len(answer[0]):
                answer[0] = word
            elif len(word) == len(answer[0]):
                for ii in range(len(word)):
                    if word[ii] > answer[0][ii]:
                        return

                answer[0] = word

            return


        def dfs(graph, node, word, answer): # graph, (a,-1), '', []
            print(f'node: {node}')
            print(f'node[0]: {node[0]}')

            if isinstance(node[0], tuple):
                print('here')
                if node[0][1] == word:
                    update_answer(word, answer)
                return

            curr_char, curr_ind = node[0], node[1] + 1 # 'a', 0 for ap


            if curr_char in graph and curr_ind in graph[curr_char] and None in graph[curr_char][curr_ind]:
                for child in graph[curr_char][curr_ind]:

                    dfs(graph, (child, curr_ind), word + curr_char, answer)

            return


        # words = ["a","banana","app","appl","ap","apply","apple"]

        graph = dict() # char: {index of char in the word: set(next_char)}
        initial_chars = set()

        for word in words: # banana
            nchars = len(word) # 6
            initial_chars.add(word[0]) # {a, b}
            for ind, char in enumerate(word): # 1, a
                if ind == nchars - 1:
                    update_graph(graph, char, ind, (None, word)) 
                else:
                    update_graph(graph, char, ind, word[ind+1])

        for char in initial_chars:
            update_graph(graph, '', -1, char)

        pp(graph)
        pp(f'initial_chars: {initial_chars}')

        answer = ['']

        for char in initial_chars:
            dfs(graph, (char, -1), '', answer)

        print(f'answer: {answer}')

        return answer[0]


    def longestWord(self, words):

        def update_result(new_word, result):
            if len(new_word) > len(result[0]):
                result[0] = new_word
            elif len(new_word) == len(result[0]):
                # import pdb; pdb.set_trace()
                for ind in range(len(new_word)):
                    if new_word[ind] < result[0][ind]:
                        result[0] = new_word
                        return
                    if new_word[ind] > result[0][ind]:
                        return

            return

        def dfs(d, char, result, words):

            if char is None:
                new_word = words[d[char]]
                update_result(new_word, result)
                return

            if None not in d[char]:
                return

            for key in d[char]:
                dfs(d[char], key, result, words)


        graph = dict()

        for ind_word, word in enumerate(words):

            if word[0] not in graph:
                graph[word[0]] = {}

            d = graph.get(word[0])

            for ind_char, char in enumerate(word):
                next_char = word[ind_char+1] if ind_char != len(word) - 1 else None
                if next_char is not None:
                    if next_char not in d:
                        d[next_char] = dict()
                else:
                    d[None] = ind_word

                d = d[next_char]

        result = ['']
        for key in graph:
            dfs(graph, key, result, words)


        return result[0]


if __name__ == "__main__":
    words = ["a","banana","app","appl","ap","apply","apple"]
    output = "apple"

    words = ["mo","moc","moch","m","mocha","l","la","lat","latt","latte","c","ca","cat", "elatte"]
    output = "latte"

    words = ["t","ti","tig","tige","tiger","e","en","eng","engl","engli","englis","english","h","hi","his","hist","histo","histor","history"]
    output = 'english'


    sol = Solution()
    print(sol.longestWord(words))
