from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks, n: int) -> int:

        if n == 0:
            return len(tasks)

        counter = Counter(tasks)
        pq = [(-count, task) for task, count in counter.items()]
        heapq.heapify(pq)
        cooldowns = dict()
        steps = 0

        # print(pq)

        while pq or cooldowns:
            steps += 1
            # print()
            # print(f'steps: {steps}')
            # print(f'pq: {pq}')
            # print(f'cooldowns: {cooldowns}')

            if len(pq) > 0:
                task = heapq.heappop(pq)
                # print(f'task: {task} pq: {pq}')

                if task[0] < -1:
                    # print(f'adding value to cooldown')
                    cooldowns[steps+n] = (task[0]+1, task[1])
                    # print(f'after addition cooldowns: {cooldowns}')

            if steps in cooldowns:
                val = cooldowns.pop(steps)
                # print(f'removing value from cooldown, val: {val}')
                heapq.heappush(pq, val)
                # print(f'after addition cooldowns: {cooldowns}')

        return steps


if __name__ == "__main__":
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]; n = 2
    output = 16

    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G","B","B","B"]; n = 2
    output = ""


    sol = Solution()
    print(sol.leastInterval(tasks, n))
