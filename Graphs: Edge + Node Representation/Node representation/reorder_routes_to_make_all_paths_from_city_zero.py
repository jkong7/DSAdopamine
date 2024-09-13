from collections import defaultdict 
from collections import deque 
class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        #Directed graph given as an edge list 
        #Only one way to travel between two different cities 
        #Return minimum number of edges changed (direction changed) so that 
        #each city can visit 0 

        #Maybe start with an undirected graph so that you can dfs the whole graph 
        self.result=0 
        visited=set()

        undirected_graph=defaultdict(list)
        for u,v in connections: 
            undirected_graph[u].append(v)
            undirected_graph[v].append(u)

        directed_graph=defaultdict(list)
        for u,v in connections: 
            directed_graph[u].append(v)


        def dfs(start): 
            #At any node start, all arrows must be pointing TO it 
            visited.add(start)
            for neighbor in undirected_graph[start]: 
                if neighbor not in visited: 
                    if neighbor in directed_graph[start]: 
                        self.result+=1 
                    dfs(neighbor)

        #BFS (just for practice): 
        def bfs(start): 
            q=deque([start])
            while q: 
                node=q.popleft()
                if node not in visited: 
                    visited.add(node)
                    for neighbor in undirected_graph[start]: 
                        if neighbor not in visited: 
                            if neighbor in directed_graph[start]: 
                                self.result+=1 
                            bfs(neighbor)

        #Iterative stack dfs (just for practice): 
        def dfs(start): 
            stack=[start]
            while stack: 
                node=stack.pop()
                if node not in visited: 
                    visited.add(node)
                    for neighbor in undirected_graph[start]: 
                        if neighbor not in visited: 
                            if neighbor in directed_graph[start]: 
                                self.result+=1 
                            dfs(neighbor)

        dfs(0)
        return self.result



