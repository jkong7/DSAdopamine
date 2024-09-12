class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        #Center will be guaranteed to in both of the first two edges
        if edges[0][0]==edges[1][0] or edges[0][0]==edges[1][1]: 
            return edges[0][0]
        else: 
            return edges[0][1]


        

        #Overkill DFS for practice:
        from collections import defaultdict
        graph=defaultdict(list)
        for u,v in edges: 
            graph[u].append(v)
            graph[v].append(u)
    
        n=len(edges)+1

        visited=set()
        def dfs(node): 
            visited.add(node)
            if len(graph[node])==n-1:
                return node 
            for neighbor in graph[node]: 
                if neighbor not in visited: 
                    result=dfs(neighbor)
                    if result: 
                        return result
            return None
        return dfs(edges[0][0])