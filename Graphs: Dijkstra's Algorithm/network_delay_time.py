import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        #This is a weighted directed graph 
        
        #Dijkstra's: 
        #Key req: Weights are NON NEGATIVE, algorithm relies on the assumption 
        #that once a vertex's shortest path is determined, it won't change 
        #Works for both weighted directed and weighted undirected graphs 
        #Dijkstra's function exactly the same, only diff is how you make 
        #adj list (function processes adj list, so diff lies in that) 
        
        #So first turn edge list into adj list 
        graph={}
        for u,v,w in times: 
            if u not in graph: 
                graph[u]=[(v,w)]
            else: 
                graph[u].append((v,w))  
                
                
        #or: 
        graph={}
        for u, v, w in times: 
            if u not in graph: 
                graph[u]=[]
            graph[u].append((v,w))
            
        #Then run dijkstras (at the end return max of distances values or -1)
        def dijkstra(start, graph): 
            pq=[(0, start)]       #Distance, vetex
            visited=set()
            distance={start: 0}   #Vertex: Distance from start     dict     
            
            while pq: 
                cur_dist, u=heapq.heappop(pq) #Pops the element with smallest distance 
            #(pq ordered by first element in tuple which is distance)
                visited.add(u)
                for v,weight in graph.get(u, []): 
                    if v not in visited: 
                        new_dist=cur_dist + weight 
                        if new_dist<distance.get(v, float('inf')): 
                            distance[v]=new_dist 
                            heapq.heappush(pq, (new_dist, v))
            return -1 if len(distance)!=n else max(distance.values())
        return dijkstra(k, graph)

        #Dijkstra's problem, the minimum time it takes for ALL n nodes to receive 
        #signal is just the max of distances dict (since if that can be reached), 
        #everything else can obviously be reached too. Distances also stores the 
        #distance from each vertex to the start including the start initialized 
        #to 0 so the len of this dict is the number of ndoes that can be reached 
        #from the start. If this doesn't equal n (total number of nodes), not every
        #node can receive the signal and thus return -1

        #Minimum time it takes for ALL n nodes to receive signal: prob just max
        #of distances dict (max(distances.values()))
        #So first turn edge list into adj list 


        #Note, don't need to even write function: 

        graph={}
        for u,v,w in times: 
            if u not in graph: 
                graph[u]=[(v,w)]
            else: 
                graph[u].append((v,w))
        
        #Dijkstras: 
        pq=[(0, k)]       #Distance, vetex
        visited=set()
        distance={k: 0}   #Vertex: Distance from start     dict     
            
        while pq: 
            cur_dist, u=heapq.heappop(pq) #Pops the element with smallest distance 
            #(pq ordered by first element in tuple which is distance)
            if u in visited: #Shortest distance for u already finalized, skip
                continue 
            visited.add(u)
            for v,weight in graph.get(u, []): 
                if v not in visited: 
                    new_dist=cur_dist + weight 
                    if new_dist<distance.get(v, float('inf')): 
                        distance[v]=new_dist 
                        heapq.heappush(pq, (new_dist, v))
        return -1 if len(distance)!=n else max(distance.values())
        
       
# Dijkstra's algorithm finds the shortest paths from a start node to all other nodes in a graph.
# It works with graphs that have non-negative edge weights.
# The algorithm uses a priority queue (min-heap) to select the node with the smallest known distance.
# Initially, the start node is set to a distance of 0, and all other nodes are set to infinity.
# The algorithm iteratively updates the shortest path estimates for each node's neighbors.
# For each node, it updates the distances to its neighbors if a shorter path is found.
# Updated nodes are added to the priority queue to be processed.
# The process continues until all reachable nodes have been processed.
# The result is a dictionary of the shortest distances from the start node to every other node.

#Always choose smallest path with an UNCLOSED node (unvisited) 
#pq will be empty once all reachable nodes have been processed and added to seen
