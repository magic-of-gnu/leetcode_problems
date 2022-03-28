from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.x2y = defaultdict(set)
        self.y2x = defaultdict(set)
        self.points = defaultdict(int)

        

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x,y)] += 1

        self.x2y[x].add(y)
        self.y2x[y].add(x)

    def _count(self, x, y, target, points):  # 11, 10, 10, {3}
        
        result = 0

        for p in points:   # {3}
            dist = target - p   # 11 - 3 = 8
            if dist == 0:
                continue

            result += self._count_squares(x, y, dist) # 11, 10, 8

        return result

    
    def _count_squares(self, x, y, dist):  # 11, 10, 8

        result = 0

        if dist > 0:
    
            # if top right
            if (x-dist,y-dist) in self.points and \
               (x     ,y-dist) in self.points and \
               (x-dist,y     ) in self.points:       
                result += self.points[(x-dist,y-dist)] * \
                          self.points[(x     ,y-dist)] * \
                          self.points[(x-dist,y     )]

            # if bot right
            if (x-dist,y+dist) in self.points and \
               (x     ,y+dist) in self.points and \
               (x-dist,y     ) in self.points:       
                result += self.points[(x-dist,y+dist)] * \
                          self.points[(x     ,y+dist)] * \
                          self.points[(x-dist,y     )]
                          
        else:

            # if top left
            if (x-dist,y-dist) in self.points and \
               (x     ,y-dist) in self.points and \
               (x-dist,y     ) in self.points:       
                result += self.points[(x-dist,y-dist)] * \
                          self.points[(x     ,y-dist)] * \
                          self.points[(x-dist,y     )]

            
            # if bot left
            if (x-dist,y+dist) in self.points and \
               (x     ,y+dist) in self.points and \
               (x-dist,y     ) in self.points:       
                result += self.points[(x-dist,y+dist)] * \
                          self.points[(x     ,y+dist)] * \
                          self.points[(x-dist,y     )]

        return result

    def count(self, point: List[int]) -> int:

        x, y = point   # 11, 10

        points_on_x = self.x2y[x]   # {2}
        points_on_y = self.y2x[y]   # {3}

        target = x                # 11
        points = points_on_y      # {3} 

        result = self._count(x, y, target, points)   # 11, 10, 10, {3}

        return result
        



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
