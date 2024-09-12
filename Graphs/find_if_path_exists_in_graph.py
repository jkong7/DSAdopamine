from collections import deque 
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """

        #Note^^No explicit graph representation, do yourself, adj list:
        if source==destination: 
            return True 

        graph={i:[] for i in range(n)} #for when n is given (# of vertices)
        for (u,v) in edges: 
            graph[u].append(v)
            graph[v].append(u)

        graph={} #Standard way to convert edge list to adj list 
        for (u,v) in edges: 
            if u not in graph: 
                graph[u]=[]
            if v not in graph:
                graph[v]=[]
            graph[u].append(v)
            graph[v].append(u)


        def bfs(graph, source, destination): 
            visited=set()
            q=deque([source])
            while q: 
                node=q.popleft()
                if node not in visited: 
                    visited.add(node)
                    if node==destination: 
                        return True 
                    for neighbor in graph[node]: 
                        if neighbor not in visited: 
                            q.append(neighbor)
            return False 
        return bfs(graph, source, destination)
                    

        def dfs(graph, source, destination): 
            visited=set()
            stack=[source]
            while stack: 
                node=stack.pop()
                if node not in visited: 
                    visited.add(node)
                    if node==destination: 
                        return True
                    for neighbor in graph[node]: 
                        if neighbor not in visited: 
                            stack.append(neighbor)
            return False
        return dfs(graph, source, destination)
        #^Iterative DFS using a stack 



        def dfs(graph, source, destination, visited=None): 
            if visited is None: 
                visited=set() #Otherwise its universal/mutable across calls 
            # Check if the current node (source) has already been visited
            if source in visited:
                # If true, it means we're revisiting a node, which we need to avoid
                # This stops the algorithm from re-exploring paths already evaluated
                # It prevents cycles, enhancing the efficiency of the DFS
                # Indicates all paths through this node were explored previously
                # Since the destination wasn't found via these paths, further exploration is unnecessary
                # Hence, we return to avoid redundant work and conserve resources
                #return is what's important, return False not nec, just convention 
                return
            if source==destination: 
                return True 
            visited.add(source)
            for neighbor in graph[source]: 
                if neighbor not in visited: 
                    if dfs(graph, neighbor, destination, visited): #Complete traversal
                        return True #Function terminates and immedtiately propogates back up True 
            return False #Never reached True after complete traversal, so no path
        return dfs(graph, source, destination)
        #^Recursive DFS 


        
        