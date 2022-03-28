from collections import deque
from pprint import pprint as pp

class MapSum:

    def __init__(self):
        self.graph = dict()
        self.cache = dict()
        self.hist = deque()
        self.words = dict()
        self.n = 10


    def insert(self, key: str, val: int) -> None:

        self.cache = dict()
        self.hist = deque()

        if key in self.words:
            self.words[key] = val
            return

        self.words[key] = val

        nchars = len(key)

        d = self.graph
        for ind, char in enumerate(key):

            if char in d:
                # print(f'here: key: {key} {d[char]["words"]}')
                # new_val = set([key]).union(d[char]['words'])
                d[char]['words'].add(key)
                # print(f'new_val: {new_val}')
            else:
                d[char] = {"words": set([key])}
                # new_val = set([key])

            # print(f'key: {key} char: {char} new_val: {new_val}')
            # d[char]["words"] = new_val

            if ind != nchars - 1:
                d = d[char]


    def sum(self, prefix):

        if prefix in self.cache:
            return self.cache[prefix]

        value = self._sum(prefix)
        if len(self.hist) == self.n:
            popleft = self.hist.popleft()

            if popleft in self.cache:
                self.cache.pop(popleft)

        self.hist.append(prefix)
        self.cache[prefix] = value
        return value


    def _sum(self, prefix: str) -> int:

        d = self.graph

        for char in prefix:
            words = d.get(char, {"words": set()})["words"]
            d = d.get(char, dict())

        # print(f'prefix: {prefix}')
        # print(f'words: {words}')

           
        val = 0
        for word in words:
            val += self.words.get(word, 0)

        return val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


if __name__ == "__main__":
    sol = MapSum()
    sol.insert("apple", 3)
    # pp(sol.graph)
    pp(sol.sum("app"))

    sol.insert("app", 2)
    # pp(sol.graph)
    pp(sol.sum("app"))

    sol.insert("apple", 2)
    pp(sol.sum("app"))

    # [[],["apple",3],["ap"],["app",2],["apple",2],["ap"]]


#    ["MapSum","insert","sum","insert","sum"]
#    [[],["a",3],["ap"],["b",2],["a"]]
#    output = [null,null,0,null,3]

# ["MapSum","insert","sum","insert","insert","sum"]
# [[],["apple",3],["ap"],["app",2],["apple",2],["ap"]]
# output = [null,null,3,null,null,4]
