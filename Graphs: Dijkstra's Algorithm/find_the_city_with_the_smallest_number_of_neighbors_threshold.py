import heapq
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        #Dijkstra's on every node in the graph 
        #Within that call, everytime a distance entry is placed into the dict, 
        #increment count if its less than distanceThreshold 

        def dijkstra(city_start, graph): 
            num_cities_smaller=0
            pq=[(0, city_start)] #Distance, vertex
            distance={city_start: 0}
            seen=set()
            while pq: 
                cur_dist, u=heapq.heappop(pq)
                if u in seen: #shortest path for u has already been finalized, skip 
                    continue 
                seen.add(u)
                for v, weight in graph.get(u, []): 
                    if v not in seen: 
                        new_dist=cur_dist+weight 
                        if new_dist<distance.get(v, float('inf')): 
                            distance[v]=new_dist
                            heapq.heappush(pq, (new_dist, v))
            num_cities_smaller=sum(1 for distance in distance.values() if distance<=distanceThreshold)
            return [num_cities_smaller, city_start] 

        graph={} #Or use defaultdict and skip the [] initializations, just append 
        for u,v,w in edges: 
            if u not in graph: 
                graph[u]=[]
            if v not in graph: 
                graph[v]=[]
            graph[u].append((v,w))
            graph[v].append((u,w))
        
        smallest, start=float('inf'), -1 

        for i in range(n): 
            num_cities_smaller, city_start=dijkstra(i, graph)
            if num_cities_smaller<smallest or (num_cities_smaller==smallest and city_start>start): 
                smallest, start=num_cities_smaller, city_start  
        return start 

        #One try (just stuck a little on sorting with the cities_smaller and the
        #city start componnets). Just use a for loop for dijkstra, unpack the 
        #two variables and then update global variables according to the two 
        #conditions 
        #Dijkstra time comp from one run: O((V+E) logV), here its from n nodes so 
        #O(n * (V+E)logV)
        #Space comp: pq, distance dict, and seen set are all O(V), graph adj list
        #is O(V+E), overall is O(V+E)

