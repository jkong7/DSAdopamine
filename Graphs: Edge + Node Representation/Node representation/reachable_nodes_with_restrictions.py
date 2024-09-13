class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        #dfs from non restricted ndoes, add to global visited as you go, keep a global 
        #max that accumulates results of connected components of non restricted nodes
        #you keep going further in a component if neigh not in visited and neigh not 
        #in restricted. Also turn restricted into a set so O(1) lookups 



        from collections import defaultdict 
        graph=defaultdict(list)
        for u,v in edges: 
            graph[u].append(v)
            graph[v].append(u)
        restricted=set(restricted)

        def dfs(node): 
            visited.add(node)
            for neighbor in graph[node]: 
                if neighbor not in visited and neighbor not in restricted: 
                    dfs(neighbor) 

        visited=set()
        dfs(0)
        return len(visited)
        