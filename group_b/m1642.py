class Solution:
    def furthestBuilding(self, heights, bricks, ladders):

        def generate_reverse_dict(d):
            return {val:key for val, key in d.items()}
        
        if len(heights) == 1:
            return 0

        l2b = {ladders:bricks}
        b2l = generate_reverse_dict(l2b)

        #            0 1 2 3 4  5  6
        # heights = [4,2,7,6,9,14,12]; bricks = 5; ladders = 1
        for ii, curr_value in enumerate(heights[:-1]): # 1, 2; 2,7; 3,6; 4,9
            next_value = heights[ii+1]     # 7; 6; 9; 14

            # print()
            # print(f'ii: {ii} curr_value: {curr_value}, next_value: {next_value}')
            # print(f'l2b: {l2b}')

            if curr_value >= next_value:
                continue

            new_l2b = dict()
            new_b2l = dict()
            diff = next_value - curr_value   # 14-9=5
            # print(f'diff: {diff}')

            # l2b = {1:5}
            # l2b = {0:5, 1:0}
            # l2b = {0:2}
            for key, value in l2b.items():   # 0:2
                # ladders
                if key > 0: # 1>0
                    a, b = max(new_b2l.get(value, 0), key) - 1 , max(new_l2b.get(key-1, 0), value)
                    new_l2b[a] = b
                    new_b2l[b] = a

                # bricks
                if value >= diff: # 17 > 16   # 10 > 8 # 5 > 3; 2 >= 5
                    a, b = key, max(new_l2b.get(key, 0), value-diff)
                    new_l2b[key] = max(new_l2b.get(key, 0), value-diff) # {0:2}

                    a, b = max(new_b2l.get(value-diff, 0), key), max(new_l2b.get(key, 0), value) - diff

            if 0 in new_l2b and new_l2b[0] == 0: # {0:2}
                new_l2b.pop(0)

            l2b = new_l2b #  {0:5, 1:0}; {0:2}
            # print(f'new_l2b: {new_l2b}')

            if not l2b:
                return ii

        return len(heights) - 1


if __name__ == "__main__":

    heights = [4,2,7,6,9,14,12]; bricks = 5; ladders = 1
    heights = [4,12,2,7,3,18,20,3,19]; bricks = 10; ladders = 2
    heights = [14,3,19,3]; bricks = 17; ladders = 0
    # heights = [9,8,5,3,2,1]; bricks = 0; ladders = 0

    # heights = [9,8,6,5,4,3,2,1]; bricks = 0; ladders = 0

    sol = Solution()
    print(sol.furthestBuilding(heights, bricks, ladders))
