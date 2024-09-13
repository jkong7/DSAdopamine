class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        #I think just when forming the graph, make it a tuple that marks whether the 
        #edge is red or blue and then when traversing, only go if its alternating 
        #and then obv if current node equals x, then at that point the path was valid 
        #so make note of value. Use bfs since its shortest path 

        from collections import defaultdict 
        from collections import deque 
        graph=defaultdict(list)
        for u,v in redEdges: 
            graph[u].append((v, 'RED'))
        for u,v in blueEdges: 
            graph[u].append((v, 'BLUE'))

        def bfs(node, visited, x):
            q=deque([(node, 0, None)])
            while q: 
                node,dist,color=q.popleft()
                if node==x: 
                    result[x]=dist 
                    break 
                for neighbor,nextcolor in graph[node]: 
                    if (node, neighbor, nextcolor) not in visited: 
                        if not color: 
                            q.append((neighbor, dist+1, nextcolor))
                            visited.add((node,neighbor, nextcolor))
                        else: 
                            if nextcolor!=color: 
                                q.append((neighbor, dist+1, nextcolor))
                                visited.add((node, neighbor, nextcolor))
        result=[-1]*n 
        for x in range(n): 
            bfs(0, set(), x)
        return result 