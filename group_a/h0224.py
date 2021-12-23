class Solution:
    def calculate2(self, s: str) -> int:
        n = len(s)

        def update_sign(sign, operator):
            if operator == '+':
                return sign

            return (sign+1)%2


        def parse_int(s, ind):

            result = []

            while ind < n and s[ind].isdigit():
                result.append(s[ind])
                ind += 1

            if not result:
                result = ['1']

            return int(''.join(result)), ind


        def eval_expr(s, ind):

            value = 0
            sign = 0 # 0 +ve, 1 -ve

            while ind < n:
                char = s[ind]

                # enter new parenthesis
                if char == '(':
                    _value, ind = eval_expr(s, ind+1)
                    value += (-1)**sign * _value
                    sign = 0

                    if s[ind] == ')':
                        ind += 1
                        continue

                if char in ops:
                    sign = update_sign(sign, char)
                    ind += 1
                    continue

                # do eval on insides
                if char == ' ':
                    ind += 1
                    continue

                # if char is a number
                if char.isdigit() is True:
                    parsed_int, ind = parse_int(s, ind)
                    value += (-1)**sign * parsed_int
                    sign = 0
                    continue

                # exit parenthesis
                if s[ind] == ')':
                    return value, ind

                ind += 1


            return value, ind

        # since no multiplication or division, we can omit the parenthesis
        ind = 0
        n = len(s)

        value = 0
        sign = 0

        ops = set('+-')
        seps = set("() ")

        while ind < n:
            _value, ind = eval_expr(s, ind)
            value += _value
            ind += 1

        return value


    def calculate(self, s: str) -> int:
        ops = set('+-*/')

        def update_st(sign, num, st):
            if sign == '+':
                st.append(int(num))
            elif sign == '-':
                st.append(int(-num))
            elif sign == '/':
                st.append(int(st.pop() / num))
            elif sign == '*':
                st.append(int(st.pop() * num))

        def calc(s, ind):
            n = len(s)

            value, st, sign = 0, [], '+'

            while ind < n:
                if s[ind].isdigit():
                    value = 10 * value + int(s[ind])
                elif s[ind] == '(':
                    value, ind = calc(s, ind+1)
                    st.append(value)
                    value, sign = 0, 0
                    if s[ind] == ')':
                        ind += 1
                    continue
                elif s[ind] in ops:
                    update_st(sign, value, st)
                    value, sign = 0, s[ind]
                elif s[ind] == ')':
                    update_st(sign, value, st)
                    return sum(st), ind

                ind += 1

            update_st(sign, value, st)
            return sum(st), ind
                
        value, ind = calc(s, 0)
        return value
        


if __name__ == "__main__":
    s = "(1+(4+5+2)-3)+(6+(-8))"
    output = 7

    s = "(1+(4+5+2)-3)+(6+8)"
    output = 23

    # s = "(1+(4+5-2)-3)+(6-(-8))"
    # output = 19

    # s = "(1+(4+5+2)-3)+(6-(-8))"
    # output = 23

    # s = "- (3 + (4 + 5))"
    # output = -12

    # s = "(7)-(0)+(4)"
    # output = 11

    sol = Solution()
    print(sol.calculate(s))
