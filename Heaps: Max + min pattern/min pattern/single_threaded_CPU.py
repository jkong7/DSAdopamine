class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """


        #Choose the one with the shortest processing time-obviously screams heap 
        #else choose the one with the smallest index, minheap (time, index)
        #The enque time can be handled easily just with a time counter I think, 
        #then the thing is greedy, it just whatever is available it gets the min
        #I think the heap can be sized to only what is available 
        #Prob use a time map for quick retrieval enque time->(index, time)
        #10^5 time screams for a soln with logn, usually BS or heap 

        import heapq 
        from collections import defaultdict 
        t=0 
        done=0
        result=[]
        heap=[]
        timemap=defaultdict(list)
        for i,task in enumerate(tasks): #O(n)
            timemap[task[0]].append((task[1], i))
        
        while len(result)<len(tasks): 
            if not heap and t in timemap: 
                for time, index in timemap[t]: 
                    heapq.heappush(heap, (time,index))
                res=heapq.heappop(heap)
                result.append(res[1])
                for _ in range(res[0]): 
                    t+=1
                    if t in timemap: 
                        for time, index in timemap[t]: 
                            heapq.heappush(heap, (time, index))
            elif heap: 
                res=heapq.heappop(heap)
                result.append(res[1])
                for _ in range(res[0]): 
                    t+=1
                    if t in timemap: 
                        for time, index in timemap[t]: 
                            heapq.heappush(heap, (time, index))
            elif not heap and t not in timemap: 
                t+=1
        return result 

        #the optimization lies in basically what I thought but didn't 
        #really know how to implement. You increment time by processtime and then 
        #every enque time within that time gets added to the queue (enque times get
        #sorted first)

        import heapq
        from collections import defaultdict

        t = 0
        result = []
        heap = []
        timemap = defaultdict(list)

        # Collect all tasks into a time map
        for i, task in enumerate(tasks):
            timemap[task[0]].append((task[1], i))

        # Get a sorted list of all enqueue times
        all_times = sorted(timemap.keys())
        time_index = 0

        while len(result) < len(tasks):
            # Push all tasks available at the current time into the heap
            while time_index < len(all_times) and all_times[time_index] <= t:
                for time, index in timemap[all_times[time_index]]:
                    heapq.heappush(heap, (time, index))
                time_index += 1

            if heap:
                # Process the task with the shortest processing time
                res = heapq.heappop(heap)
                result.append(res[1])
                t += res[0]
            else:
                # Move to the next time with available tasks
                if time_index < len(all_times):
                    t = all_times[time_index]
                else:
                    break  # This handles the case where no more tasks are available in the future

        return result

        