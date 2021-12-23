class Solution:
    def compareVersion2(self, version1: str, version2: str) -> int:

        def generate_version(version, start_ind):

            if start_ind > len(version):
                return 0, start_ind + 1

            # version1
            # 1.01    1

            # version2
            # 1.001    1

            while version[start_ind] == ".":    # version[3] = 1,   version[1] = .
                start_ind += 1

            # start_ind = 2
            st = ""
            new_start_ind = len(version)

            for ind, char in enumerate(version[start_ind:], start=start_ind):  

                if char == '.':
                    new_start_ind = ind
                    break
                elif (st == "" and char != "0") or st != "":
                    st += char

            if not st:
                st = '0'

            return int(st), new_start_ind + 1

        start_ind1 = 0
        start_ind2 = 0
        n1, n2 = len(version1), len(version2)

        while start_ind1 < n1 or start_ind2 < n2:      # 0    0;  1   1;  3  4
            v1, start_ind1 = generate_version(version1, start_ind1)   # 1,   2;  1   4;
            v2, start_ind2 = generate_version(version2, start_ind2)   # 1,   2;  1   5;

            if v1 == v2:
                continue
            elif v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        return 0



if __name__ == "__main__":

    ver1 = "0.001"
    ver2 = "0.002"

    ver1 = "1.01"
    ver2 = "1.001"

    ver1 = "1.01.0"
    ver2 = "1.001"

    ver1 = "1.0.1"
    ver2 = "1"

    ver1 = "1.0"
    ver2 = "1.0.0"

    ver1 = "1.1"
    ver2 = "1.10"

    sol = Solution()
    print(sol.compareVersion(ver1, ver2))
