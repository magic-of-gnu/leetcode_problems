class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3
        elif n == 2:
            return 8
        
        s1, s2, s3 = 1,0,3
        s4, s5, s6 = 1,1,2
        
        for __ in range(2,n):
            _s = s4+s5+s6
            s1,s2,s3,s4,s5,s6 = \
                s3,\
                s1,\
                (s1+s2+s3+_s)% (1000_000_007),\
                s6,\
                s4,\
                _s% (1000_000_007)
            
        
# 1) single A but ends on single L - add L -> 2
#                                  - add P -> 3
# 2) single A but ends on double L - add P -> 3
# 3) single A but does end on L    - add L -> 1
#                                  - add P -> 3
    
# 4) no A but ends on single L     - add A -> 3
#                                  - add L -> 5
#                                  - add P -> 6
# 5) no A but ends on double L     - add A -> 3
#                                  - add P -> 6
# 6) no A does not end on L        - add A -> 3
#                                  - add L -> 4
#                                  - add P -> 6
      
# graph
# 1 -> 2,3
# 2 -> 3
# 3 -> 1, 3
# 4 -> 3, 5, 6
# 5 -> 3, 6
# 6 -> 3, 4, 6

# rev_graph
# 1 -> 3
# 2 -> 1
# 3 -> 1, 2, 4, 5, 6, 3
# 4 -> 6
# 5 -> 4
# 6 -> 4, 5, 6
            

        return (s1+s2+s3+s4+s5+s6) % (1000_000_007)
