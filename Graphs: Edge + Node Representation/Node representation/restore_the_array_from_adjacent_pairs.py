class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        #A number can never appear in more than two pairs 
        #So if we have two pairs with a number in common, that number HAS to go in the
        #middle 

        #There are only two nums that will appear only once in the adjacentPairs, these 
        #nums are the ends 


        from collections import defaultdict
        graph=defaultdict(list) 
        for u,v in adjacentPairs: 
            graph[u].append(v) 
            graph[v].append(u) 

        def dfs(node): 
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]: 
                if neighbor not in visited: 
                    dfs(neighbor)
        visited=set()
        result=[]
        for node in graph: 
            if len(graph[node])==1: 
                dfs(node)
                break 
        return result 

        #Yep just form the bidirectional graph and then there are two nodes you can start
        #the dfs on which are the ends, these are the ones with only one neighbor 