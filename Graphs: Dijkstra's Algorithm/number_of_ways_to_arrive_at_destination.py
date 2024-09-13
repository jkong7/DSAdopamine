import heapq
from collections import defaultdict 
class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        #CAN reach any node from any other node so don't have to worry about that 
        #like the return -1 in "network delay time"
        #Given edge list (u,v,w) BIDIRECTIONAL, so WEIGHTED UNDIRECTED GRAPH 
        #Start: 0 
        #End: n-1  distance[n-1] will be shortest path from 0 to n-1 
        #But question doesn't just ask for what is that shortest path, its asking 
        #how many ways can get from 0 to n-1 IN that shortest path 

        #Djikstras with pred dict (that can store multiple pred), then call a 
        #recursive function on pred dict that finds numb of min paths from start 
        #to end 

        #1. Convert edge list to adj list 
        MOD=(10**9 +7)
        graph=defaultdict(list)
        for u,v,w in roads: 
            graph[u].append((v,w))
            graph[v].append((u,w))
        #2. Dijkstras that can return distance, and pred (multiple pred allowed)
        #If new_dist==distance[v], append u to the already made dict entry [v]->[u]
        def dijkstra(graph, start): #Returns distance, pred 
            pq=[(0, start)] #distance, vertex
            distance={start: 0}
            pred=defaultdict(list)
            pred[start]=[None]
            while pq: 
                cur_distance, u=heapq.heappop(pq)
                if u in distance and cur_distance>distance.get(u, float('inf')): 
                    continue 
                for v,weight in graph.get(u, []): 
                    new_distance=cur_distance+weight
                    if new_distance<distance.get(v, float('inf')): 
                        distance[v]=new_distance 
                        pred[v]=[u]
                        heapq.heappush(pq, (new_distance, v))
                    elif new_distance==distance[v]: 
                        pred[v].append(u)
            return pred
        #3. Recursive function that increments a 1 if a path from end can be 
        #backtracked to start, will be the final return statement 
        def num_of_paths(predec, start, end, memo):
            if end in memo:
                return memo[end]
            if start == end:
                return 1
            if not predec[end]:
                return 0
            total_paths = sum(num_of_paths(predec, start, pred, memo) for pred in predec[end]) % MOD
            memo[end] = total_paths
            return total_paths

        pred = dijkstra(graph, 0)
        memo = {}
        return num_of_paths(pred, 0, n - 1, memo)

        #Got it, works but was getting TLE, the recursive function was not efficient
        #nough, needed to use memoization (haven't learned it yet)
        







#dijkstra's with path (predecessor dict) just two additional lines, initialization 
#{start:None} and predecessors[v]=u   ASSUMES EACH NODE HAS AT MOST ONE PRED 
import heapq
def dijkstra_with_paths(graph, start):
    pq = [(0, start)]  # Priority queue initialized with (distance, vertex)
    distances = {start: 0}  # Dictionary to store the shortest known distances
    predecessors = {start: None}  # Dictionary to store the predecessor of each node
    visited = set()  # Set to track visited vertices

    while pq:
        cur_dist, u = heapq.heappop(pq)  # Pop the vertex with the smallest distance from the priority queue
        if u in visited:
            continue
        visited.add(u)  # Mark the vertex as visited

        for v, weight in graph.get(u, []):  # Update the distances to each neighbor
            if v not in visited:
                new_dist = cur_dist + weight
                if new_dist < distances.get(v, float('inf')):  # Using .get to handle default value of inf
                    distances[v] = new_dist
                    predecessors[v] = u  # Set the predecessor of v to u
                    heapq.heappush(pq, (new_dist, v))  # Push the updated distance to the priority queue

    return distances, predecessors

def reconstruct_path(predecessors, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()  # Reverse the path to get the correct order from start to end
    if path[0] == start:
        return path
    else:
        return []  # If the start node is not at the beginning of the path, no path exists

