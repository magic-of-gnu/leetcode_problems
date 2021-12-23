from pprint import pprint as pp


class Solution:
    def shortestSuperstring(self, words):

        def create_node(graph, char):
            if char not in graph:
                graph[char] = {
                    "start": set(),
                    "end": set(),
                    "current_char": set(),
                    "next_char": set(),
                }


        graph = dict()

        for iw, word in enumerate(words):

            last_char = word[0]
            last_ic = 0

            create_node(graph, last_char)

            graph[last_char]["start"].add(iw)
            graph[last_char]["current_char"].add(tuple([iw, last_ic]))

            if len(word) == 1:
                graph[last_char]["end"].add(iw)

            for ic, char in enumerate(word[1:], start=1):
                graph[last_char]["next_char"].add(char)

                create_node(graph, char)

                graph[char]["current_char"].add(tuple([iw, ic]))
                if ic == len(word) - 1:
                    graph[char]["end"].add(iw)

                last_char = char

        pp(graph)

        # bfs would be good
        graph_suffix = dict()

        for iw, word in enumerate(words):

            last_char = word[0]
            last_ic = 0
            # current_words = set()  # (iw, ic)
            current_words = dict() # iw
            # print()
            # print()
            # print(f'iw: {iw} word: {word}')

            for ic, char in enumerate(word[1:], start=1):
                node = graph[char]
                _current_words = dict()
                # print()
                # print(f'ic: {ic} char: {char}')
                # pp(node)
                # print(f'current_words: {current_words}')
                # check what we have right now
                for _iw, _ic in current_words.items():
                    if _iw in node['end'] and _ic == len(words[_iw]):
                        #print('end detected')
                        True
                    elif (_iw, _ic) in node['current_char']:
                        _current_words[_iw] = _ic + 1

                # add new words
                new_words = node['start'] - set([iw])
                for new_word in new_words:
                    _current_words[new_word] = 1
                current_words = _current_words

            graph_suffix[iw] = current_words

        pp(graph_suffix)

        result = []
        counter = [len(word) for word in words]
        n = sum(counter)
        nwords = len(words)
        best_result = []
        n_best = n

        def dfs(graph_suffix, current_path, node, best_len, best_result):

            # if not node:
            #     return

            # all words are in the path
            if len(current_path) == nwords:
                result = "".join([words[iw][ic:] for iw, ic in current_path.items()])
                if (best_len[0] is None and best_result[0] is None) or len(result) < best_len[0]:
                    best_result[0] = result
                    best_len[0] = len(result)

                # print(f'current_path: {current_path}')
                # print(f'result word: {result}')

            children_nodes = dict()
            _nodes = graph_suffix[node]
            for x in range(nwords):
                if x in current_path or x == node:
                    continue

                children_nodes[x] = _nodes.get(x, 0)


            for iw, ic in children_nodes.items():

                current_path[iw] = ic

                dfs(graph_suffix, current_path, iw, best_len, best_result)

                # print(f'current_path: {current_path}')
                # print(f'current_score: {current_score}')

                current_path.pop(iw)

        paths = []

        best_len = [None]
        best_result = [None]

        for iw, word in enumerate(words):
            dfs(graph_suffix, {iw:0}, iw, best_len, best_result)

        # print(f'best_len: {best_len}')
        # print(f'best_result: {best_result}')



if __name__ == "__main__":
    words = ["catg","ctaagt","gcta","ttca","atgcatc"]
    Output = "gctaagttcatgcatc"

    words = ["gruuz","zjr","uuzj","rfgr"]
    Output = "rfgruuzjr"

    sol = Solution()
    print(sol.shortestSuperstring(words))
