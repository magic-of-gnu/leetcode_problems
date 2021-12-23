class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        def get_steps(start, end, n):

            dist0 = abs(end - start)
            dist1 = n - dist0

            return min(dist0, dist1)

        def dfs(graph, key, gii, kjj, min_count, current_count, seen, n):

            # current_count += current_steps

            if kjj == len(key):
                # finished
                min_count[0] = min(min_count[0], current_count)
                return

            print()
            print(f'gii: {gii} kjj: {kjj} key[kjj]: {key[kjj]}')
            print(f'current_count: {current_count}')
            print(f'min_count: {min_count}')


            for child in graph[key[kjj]]: # if multiple identical letters in the word
                current_steps = get_steps(gii, child, n)
                print(f'child: {child} current_steps: {current_steps}')

                dfs(graph, key, child, kjj+1, min_count, current_count + current_steps, n)

            return

        nring = len(ring)
        graph = dict()

        for ind, char in enumerate(ring):
            if char in graph:
                graph[char].append(ind)
            else:
                graph[char] = [ind]

        min_count = [len(key)*len(ring)]

        dfs(graph, key, 0, 0, min_count, 0, nring)

        return min_count[0] + len(key)



if __name__ == "__main__":
    # ring = "godding"; key = "godding"
    output = 13
    ring = "fallout"; key = "fall"
    output = 6

    sol = Solution()
    print(sol.findRotateSteps(ring, key))
