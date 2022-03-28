import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        def assign_task(next_tasks, task2ind, curr_time, current_state, results):
            new_task = next_tasks[0]  # 2
            task_ind = heapq.heappop(task2ind[new_task])  # 1

            if not task2ind[new_task]:
                task2ind.pop(new_task)
                heapq.heappop(next_tasks)

            results.append(task_ind)
            
            if current_state is not None:
                current_state[0] = False
                current_state[1] = curr_time + new_task
            
            return
        
        tasks = [(enqTime, procTime, ind) for ind, (enqTime, procTime) in enumerate(tasks)]
        
        tasks = list(sorted(tasks, key=lambda x: x[0]))
        
        next_tasks = []
        task2ind = defaultdict(list)
        results = []

        current_state = [True, None]  # if idle, task finish time
        n = len(tasks)
        curr_time = 0
        ii = 0
        

        while ii < n:  # 0
            
            while ii < n and curr_time == tasks[ii][0]:  # 1 vs 1
                if tasks[ii][1] not in task2ind:  # 2 
                    heapq.heappush(next_tasks, tasks[ii][1])  
                heapq.heappush(task2ind[tasks[ii][1]], tasks[ii][2])
                ii += 1   # 1

            if current_state[1] == curr_time:
                current_state[0] = True

            if current_state[0] is True and next_tasks:

                assign_task(next_tasks, task2ind, curr_time, current_state, results)

            curr_time += 1

        while next_tasks:
            assign_task(next_tasks, task2ind, curr_time, current_state, results)
            
        return results


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        if len(tasks) == 1:
            return [0]

        def push_to_inds(task2ind, task):
            heapq.heappush(task2ind[task[1]], task[2])

            return

        def get_next_task(next_tasks, task2ind):
            task_proc_time = next_tasks[0]
            task_ind = heapq.heappop(task2ind[task_proc_time])

            if not task2ind[task_proc_time]:
                task2ind.pop(task_proc_time)
                heapq.heappop(next_tasks)

            return task_proc_time, task_ind

        tasks = [(enqTime, procTime, ind) for ind, (enqTime, procTime) in enumerate(tasks)]

        tasks = list(sorted(tasks, key=lambda x: x[0]))


        next_tasks = []
        task2ind = defaultdict(list)
        results = []

        n = len(tasks)
        curr_time = 0
        ii = 0
        while ii < n:

            while ii < n and curr_time >= tasks[ii][0]:
                task = tasks[ii]

                if task[1] not in task2ind:
                    heapq.heappush(next_tasks, task[1])

                push_to_inds(task2ind, task)
                ii += 1

            if next_tasks:
                task_proc_time, task_ind = get_next_task(next_tasks, task2ind)
                results.append(task_ind)

                curr_time += task_proc_time

            else:
                curr_time = tasks[ii][0]

        while next_tasks:
            task_proc_time, task_ind = get_next_task(next_tasks, task2ind)
            results.append(task_ind)

        return results

    
    
            
