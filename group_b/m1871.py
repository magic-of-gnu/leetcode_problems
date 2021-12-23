class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        if s[-1] == '1':
            return False

        def is_valid_jump(s, ii, n, jump):

            if not(0 <= ii - jump < n):
                return False

            if s[ii - jump] == '1':
                return False

            return True


        seen = [int(char) for char in s]
        seen[0] = -1
        n = len(s)

        for ii in range(minJump, n):
            if s[ii] == '1':
                continue

            for jump in range(minJump, maxJump+1):
                if not is_valid_jump(s, ii, n, jump):
                    continue

                if seen[ii - jump] == -1:
                    seen[ii] = -1
                    break

            if jump == maxJump and seen[ii] != -1:
                print(f'here, ii: {ii}')
                print(f'seen: {seen}')
                break

        return seen[-1] == -1


    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        if s[-1] == '1':
            return False

        def is_valid_jump(s, ii, n, jump):

            if not(0 <= ii + jump < n):
                return False

            if s[ii + jump] == '1':
                return False

            return True

        seen = [int(char) for char in s]
        seen[0] = -1
        n = len(s)

        for ii in range(n):
            if s[ii] == '1':
                continue

            for jump in range(minJump, maxJump + 1):
                if is_valid_jump(s, ii, n, jump):
                    seen[ii+jump] = -1

        return seen[-1] == -1





if __name__ == "__main__":

    s = "011010"; minJump = 2; maxJump = 3
    Output = True

    # s = "01101110"; minJump = 2; maxJump = 3
    # Output = False

    # s = "0000000000"
    # minJump = 2
    # maxJump = 5

    sol = Solution()
    print(sol.canReach(s, minJump, maxJump))
