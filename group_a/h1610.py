import math


class Solution:
    # def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
    def visiblePoints(self, points, angle: int, location) -> int:

        def calculate_angles(location, points):

            angles = []
            repitions = {0:0}
            points_on_location_count = 0

            for point in points:
                if point[0] == location[0] and point[1] == location[1]:
                    points_on_location_count += 1
                    continue

                dx, dy = point[0] - location[0], point[1] - location[1]

                alpha = math.atan2(dy, dx)

                if alpha < 0:
                    alpha = math.pi + math.pi + alpha # -1/1 -> -45 -> 180 + (180-45) = 180 + 135

                alpha = math.degrees(alpha)

                if alpha in repitions:
                    repitions[alpha%360] += 1
                else:
                    repitions[alpha%360] = 1
                    # angles.append(alpha)

            # angles.sort()

            # if angles[0] != 0:
            #     angles = [0] + angles

            return angles, repitions, points_on_location_count


        angles, repetitions, points_on_location_count = calculate_angles(location, points)
        print(f'angles: {angles}')
        print(f'repetitions: {repetitions}')
        print(f'points_on_location_count: {points_on_location_count}')

        l, r = 0, 0
        result = 0
        n = len(repetitions)
        curr = 0
        max_result = 0

        sorted_angles = list(sorted(repetitions.keys()))

        for l in range(n):

            print()
            print(f'l: {l} r: {r} result: {result} max_result: {max_result}')

            while r < n and sorted_angles[r] - sorted_angles[l] <= angle:
                result += repetitions[sorted_angles[r]]
                max_result = max(max_result, result)
                r += 1

            while r >= n and 360 + sorted_angles[r%n] - sorted_angles[l] <= angle:
                result += repetitions[sorted_angles[r%n]]
                max_result = max(max_result, result)
                r += 1

            result -= repetitions[sorted_angles[l]]

        return max_result + points_on_location_count
            

if __name__ == "__main__":
    points = [[2,1],[2,2],[3,3]]; angle = 90; location = [1,1]

    sol = Solution()

    print(sol.visiblePoints(points, angle, location))
