from collections import defaultdict
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n=len(graph)
        self.result=[]
        def dfs(start, end, path): 
            path=path+(start,)
            if start==end: 
                self.result.append(list(path))
            for neighbor in graph[start]: 
                dfs(neighbor, end, path)
        dfs(0, n-1, ())
        return self.result


        mygraph=defaultdict(list)
        for i in range(len(graph)): 
            mygraph[i]=graph[i]
        n=len(mygraph)
        self.result=[]
        def dfs(start, end, path): #Path needs to be immutable 
            path=path+(start,)
            if start==end: 
                self.result.append(list(path))
            for neighbor in mygraph[start]: 
                dfs(neighbor, end, path)
        dfs(0, n-1, ())
        return self.result 