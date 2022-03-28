class Solution:
    def minFlips(self, mat):

        # 0 1
        # 2 3

        # 0 0     1 1
        # 0 1     0 0

        # 1 1     0 0
        # 1 1     1 0

        # 3210
        # 0 -> _210  7
        # 1 -> 3_10  11
        # 2 -> 32_0  13
        # 3 -> 321_  14
        
        m, n = len(mat), len(mat[0])
        
        flip_map = {}
        
        counter = 0
        init_state = 0
        for ii in range(m):
            for jj in range(n):
                flip_map[(ii,jj)] = counter
                init_state = init_state ^ (mat[ii][jj] << counter)

                counter += 1
                
        next_jumps = dict()
        for (ii,jj), v in flip_map.items():
            next_jumps[v] = (1 << v)
            for di, dj in [(-1,0), (0,1), (1,0), (0,-1)]:
                ni, nj = ii+di, jj+dj

                if (ni,nj) not in flip_map:
                    continue
                next_jumps[v] = next_jumps[v] ^ (1 << flip_map[(ni,nj)])

        states = {init_state:0}  # 8 : 0
    
        for cur_jump in range(v+1):  # 3
            new_states = dict()    
            for s in states:       # 8
                #          8^14 - > 9
                next_state = s^next_jumps[cur_jump]
                new_states[next_state] = min(states[s] + 1, states.get(next_state, n*m))

            states.update(new_states) # 8:0  15:1 3:1 4:2

        if 0 in states:
            return states[0]

        return -1

        

if __name__ == "__main__":
    
    mat = [[0,0],[0,1]]
    mat = [[0,1,0],[1,1,1]]

    sol = Solution()
    print(sol.minFlips(mat))
