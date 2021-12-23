from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:

        def valid_path(a, b):
            if len(a) == len(b):
                n = 0
                for ii in range(len(a)):
                    if a[ii] != b[ii]:
                        n += 1

                    if n == 2:
                        return False


            elif abs(len(a) - len(b)) == 1:
                n = 0 
                for ii in range(min(len(a), len(b))):
                    if a[ii] != b[ii]:
                        n += 1

                    if n == 1:
                        return False


            elif abs(len(a) - len(b)) > 1:
                return False

            return True

        if valid_path(beginWord, endWord):
            for word in wordList:
                if endWord == word:
                    return 2
            return 0

        def add_path(a, b, graph):
            if valid_path(a, b):
                graph[a].add(b)
                graph[b].add(a)
                return True

            return False

        def construct_graph(b, e, wordList):
            graph = defaultdict(set)
            is_valid_end = False

            for word in wordList:
                add_path(b, word, graph)
                is_valid_end = is_valid_end | (e == word)

            if is_valid_end is False:
                return False

            for ii in range(len(wordList)-1):
                for jj in range(ii+1, len(wordList)):
                    add_path(wordList[ii], wordList[jj], graph)

            return graph


        def traverse(graph, node, current_path, seen, min_count, endWord):
            if node is None:
                return False

            if node in current_path:
                return False

            if node in seen:
                if seen[node] is False:
                    return False

                return True


            current_path.add(node)
            end_visited = False

            for child in graph[node]:
                if child == endWord:
                    if min_count[0] is False:
                        min_count[0] = len(current_path) + 1
                    min_count[0] = min(min_count[0], len(current_path)+1)
                    current_path.discard(node)
                    seen[node] = 2
                    return True

                result = traverse(graph, child, current_path, seen, min_count, endWord)
                end_visited = end_visited | result

                if result is True:
                    seen[node] = min(seen[child]+1, seen.get(node, seen[child]+1))
                    min_count[0] = min(min_count[0], seen[child] + len(current_path))

            current_path.discard(node)
            if end_visited is False:
                seen[node] = False
            return end_visited

        graph = construct_graph(beginWord, endWord, wordList)
        if graph is False:
            return 0

        min_count = [False]
        seen = dict()

        traverse(graph, beginWord, set(), seen, min_count, endWord)

        if min_count[0] is False:
            return 0

        return min_count[0]




if __name__ == "__main__":
    beginWord = "hit"; endWord = "cog"; wordList = ["hot","dot","dog","lot","log","cog"]
    beginWord = "hit"; endWord = "cog"; wordList = ["hot","dot","dog","lot","log"]

    beginWord = "hot"; endWord = "dog"; wordList = ["hot","dog"]
    beginWord = "a"; endWord = "z"; wordList = ["b"]

    beginWord = "qa"
    endWord = "sq"
    wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]

    sol = Solution()
    print(sol.ladderLength(beginWord, endWord, wordList))
