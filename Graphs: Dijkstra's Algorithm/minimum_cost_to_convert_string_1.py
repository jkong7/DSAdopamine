class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        #The original to changed with cost can be rep as a weighted directed graph 

        from collections import defaultdict 
        import heapq 
        graph=defaultdict(list)
        for i in range(len(original)): 
            graph[original[i]].append((changed[i], cost[i]))

        memo={}
        def djik(start, dest): 
            if (start, dest) in memo: 
                return memo[(start, dest)]
            pq=[(0, start)] #distance, vertex
            distance={start: 0}
            visited=set()

            while pq: 
                cur_dist, u=heapq.heappop(pq)
                if u not in visited: 
                    visited.add(u)
                    for v,w in graph.get(u, []): 
                        if v not in visited: 
                            new_dist=cur_dist+w
                            if new_dist<distance.get(v, float('inf')): 
                                distance[v]=new_dist 
                                heapq.heappush(pq, (new_dist, v))
            for node in distance: 
                memo[(start, node)]=distance[node] if node in distance else -1 
            return distance[dest] if dest in distance else -1 
        
        total=0 
        for i in range(len(source)): 
            if source[i]!=target[i]: 
                path=djik(source[i], target[i])
                if path==-1: 
                    return -1 
                total+=path 
        return total 

        #YUP and you can memoize even further, djik calculates the paths from start 
        #to ALL other nodes so why dont't we take advantage of that and memoize all the
        #paths (just use a for loop for the nodes in distance and store all of them). 
        #Holy bumps the TC up to beats 100% lmao 