class Solution:

    def parseBoolExpr(self, expression: str) -> bool:

        ops = set("!&|")
        vals = {"t": True, "f": False}

        def find_brackets(expr, start_ind):

            # print()
            # print(f'find bracket called; start_ind: {start_ind}')

            args = []
            op = None
            if expr[start_ind] in ops:
                op = expr[start_ind]
                start_ind += 1

            ind = start_ind


            while ind < len(expr) and expr[ind] != ")":
                char = expr[ind]
                # print(f'ind: {ind} char: {char} op: {op}')

                if char in ops:
                    # print(f'calling find_brackets, op: {op}, ind: {ind}')
                    value, ind = find_brackets(expr, ind)
                    args.extend(value)
                elif char in vals:
                    args.append(vals[char])

                ind += 1

            if op is None:
                return args, ind

            return [do_operation(op, args)], ind

        def do_operation(op, args):
            # print()
            # print(f'do operation is called: op: {op} args: {args}')
            if op == "&":
                val = True
                for _val in args:
                    if (val & _val) is False:
                        return False
                return True

            elif op == "|":
                val = False
                for _val in args:
                    val |= _val

                return val

            elif op == "!":
                if len(args) > 1:
                    raise ValueError("there is no more than 1 arg in operation '!'")
                return not args[0]

        val, ind = find_brackets(expression, 0)
        return val[0]
        

if __name__ == "__main__":
    #                       111111
    #             0123456789012345
    expression = "|(&(t,f,t),!(t))"
    expression = "|(&(t,f,t),!(t))"
    output = False

    sol = Solution()
    print(sol.parseBoolExpr(expression))
