class Solution:
    def maximumSwap(self, num: int) -> int:
        value = str(num)
        n = len(value)

        max_idx = n-1
        result = list(range(n))

        for idx in reversed(range(n)):

            if value[idx] > value[max_idx]:
                max_idx = idx
            elif value[idx] < value[max_idx]:
                results[idx] = max_idx

        for idx in range(n):
            if idx != results[idx]:
                break


        tmp = results[idx]
        results[tmp] = idx

        val = list(range(n))
        val[tmp] = idx
        val[idx] = tmp

        val = int(''.join([value[x] for x in val]))


        return val


if __name__ == "__main__":
    num = 2736
    output = 7236

    num = 919
    num = 991
    num = 9876543211111

    num = 98368

    sol = Solution()
    print(sol.maximumSwap(num))
