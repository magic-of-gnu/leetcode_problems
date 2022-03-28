
class Solution:
    def findReplaceString(self, s, indices, sources, targets):

        to_be_replaced = [-1]*len(s)

        for ii, (ind, source, target) in enumerate(zip(indices, sources, targets)):
            if s[ind:].startswith(source):
                # print()
                # print(f'ii: {ii}')
                # print(f'ind: {ind} source: {source} target: {target}')
                to_be_replaced[ind] = target
                for ind_target, char in enumerate(source[1:], start=ind+1):
                    to_be_replaced[ind_target] = 0

        result = []
        for ind, val in enumerate(to_be_replaced):
            if val == -1:
                result.append(s[ind])
            elif val != 0:
                result.append(val)
        return ''.join(result)


if __name__ == "__main__":

    s = "abcd"; indices = [0, 2]; sources = ["a", "cd"]; targets = ["eee", "ffff"]

    sol = Solution()
    print(sol.findReplaceString(s, indices, sources, targets))
