class Solution:

    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) == 3:
            return int(num[0]) + int(num[1]) == int(num[2])

        def calc_valid(num, ind, sep0, sep1):

            num0 = num[ind:sep0] # 1
            num1 = num[sep0:sep1] # 9

            nsum = str(int(num0) + int(num1)) # 10
            sep2 = sep1 + len(nsum)

            if (num0[0] == '0' and len(num0) > 1) or (num1[0] == '0' and len(num1) > 1):
                return False, sep2

            ssum = num[sep1:sep2]  # num[2:4]

            if nsum == ssum:
                return True, sep2

            return False, sep2

        ind = 0
        sep0, sep1 = 1, 2
        n = len(num)

        for sep0 in range(ind+1, n-1):
            for sep1 in range(sep0+1, n):

                _ind, _sep0, _sep1 = ind, sep0, sep1
                _sep2 = _sep1 + 1

                while _sep1 < n and _sep2 < n:
                    is_valid, _sep2 = calc_valid(num, _ind, _sep0, _sep1)

                    if is_valid is True:
                        _ind = _sep0
                        _sep0 = _sep1

                    _sep1 += 1

                if is_valid is True:
                    return is_valid

        return is_valid



if __name__ == "__main__":
    #    012345678
    s = "199100199"
    output = True

    s = "123"
    output = True

    s = "1023"
    output = False

    s = "211738"
    output = True

    s = "0235813"
    output = False

    s = "011235"
    output = True

    sol = Solution()
    print(sol.isAdditiveNumber(s))
        
