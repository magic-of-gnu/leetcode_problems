class Solution:
    def solveEquation(self, equation: str) -> str:

        seps = set('+-="')

        def parse(s, ind):

            result = []
            t = 0

            while ind < len(s) and s[ind] not in seps:
                if s[ind] == 'x':
                    t = 1
                else:
                    result.append(s[ind])
                ind += 1

            if not result:
                result = ['1']

            return int(''.join(result)), t, ind

        s = equation

        ind = 0
        clhs, xlhs = 0, 0
        crhs, xrhs = 0, 0
        sign = 0

        ans_inf = "Infinite solutions"
        ans_nos = 'No solution'
        n = len(s)

        while ind < n:

            if s[ind] == '=':
                clhs = crhs
                xlhs = xrhs

                crhs, xrhs = 0, 0
                sign = 0

            if s[ind] == '-':
                sign = 1
            elif s[ind] == '+':
                sign = 0

            if s[ind] in seps:
                ind += 1
                continue

            val, t, ind = parse(s, ind)
            if t == 0:
                crhs += (-1)**sign * val
            elif t == 1:
                xrhs += (-1)**sign * val

        # print(f'clhs: {clhs} crhs: {crhs}')
        # print(f'xlhs: {xlhs} xrhs: {xrhs}')

        if clhs == crhs:
            if xlhs == xrhs:
                return ans_inf
            else:
                return "x=0"
        else:
            if xlhs == xrhs:
                return ans_nos
            else:
                return f"x={int((crhs - clhs) / (xlhs - xrhs))}"

        # end of equation


if __name__ == "__main__":
    equation = "x+5-3+x=6+x-2"
    output = "x=2"

    equation = "2x+3x-6x=x+2"
    equation = "2x+3x-6x=-2x+2"

    sol = Solution()
    print(sol.solveEquation(equation))
