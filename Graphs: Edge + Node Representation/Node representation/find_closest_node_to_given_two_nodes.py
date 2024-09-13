class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """
        #Each node has at most once outgoing edge (ie only one neighbor) 
        #Neighbor of node i is edges[i]

        #Why dont we just a full graph traversal from both of the nodes and fill in 
        #two result arrays where the index rep the dist to the node and -1 if it cant
        #be reached (just init with -1). Then at the end just traverse them and do 
        #the condition, super easy at that point 

        #Either bfs or dfs work here 
        from collections import defaultdict
        graph=defaultdict(list)
        for i in range(len(edges)): 
            if edges[i]!=-1: 
                graph[i].append(edges[i])

        def dfs(node, result, visited, count):
            visited.add(node) 
            result[node]=count 
            for neighbor in graph[node]: 
                if neighbor not in visited: 
                    dfs(neighbor, result, visited, count+1)

        result1, result2=[-1]*len(edges), [-1]*len(edges)
        visited1, visited2=set(),set()
        dfs(node1, result1, visited1, 0)
        dfs(node2, result2, visited2, 0)

        minn=float('inf')
        result=-1 
        for i in range(len(result1)): 
            if result1[i]!=-1 and result2[i]!=-1: 
                dist=max(result1[i], result2[i])
                if dist<minn: 
                    minn, result=dist, i
                elif dist==minn: 
                    if i<result: 
                        result=i 
        return result 

