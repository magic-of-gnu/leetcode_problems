class Solution:
    def lengthLongestPath(self, s: str) -> int:

        st = []
        max_result = ''
        nmax = 0

        def is_file(s):
            is_dot_here = False
            for char in reversed(s):
                if char == '.':
                    is_dot_here = True
                elif char == '/':
                    break
            
            return is_dot_here


        def get_max_result(max_result, nmax, st):
            joined = '/'.join([x[0] for x in st])

            if is_file(joined) is False:
                return max_result, nmax

            if nmax < len(joined):
                return joined, len(joined)

            return max_result, nmax


        for line in s.split("\n"):

            # count num of \t
            count = 0
            while line[count] == '\t':
                count += 1

            text = line[count:]

            while st and not(st[-1][1] < count):
                st.pop()

            st.append((text, count))
            max_result, nmax = get_max_result(max_result, nmax, st)

        return nmax


if __name__ == "__main__":
    s = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext\n\t\tdeqweqweqwewq"
    output = 20

    sol = Solution()
    print(sol.lengthLongestPath(s))
