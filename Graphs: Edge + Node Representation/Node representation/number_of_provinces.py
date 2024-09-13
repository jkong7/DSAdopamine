class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        #Number of connected components given an adj matrix 
        graph=defaultdict(list)
        n=len(isConnected)
        for i in range(n): 
            for j in range(n): 
                if isConnected[i][j]==1: 
                    graph[i].append(j)
        self.result=0
        visited=set()
        def graph_iterator(graph): 
            for i in graph: 
                if i not in visited: 
                    self.result+=1 
                    dfs(i)
        def dfs(start): 
            visited.add(start)
            for neighbor in graph[start]: 
                if neighbor not in visited: 
                    dfs(neighbor)
        graph_iterator(graph)
        return self.result