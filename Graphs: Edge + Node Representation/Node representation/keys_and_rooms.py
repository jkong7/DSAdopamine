from collections import defaultdict 
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        #Make it into an adj list representation, then do dfs on room 0, if it can 
        #reach every node (one connected component), return true. If len(visited)
        #equals n, that means we saw everything so true in that case
        graph=defaultdict(list)
        for i in range(len(rooms)): 
            graph[i]=rooms[i]
        n=len(rooms)
        
        visited=set()
        def dfs(start): 
            visited.add(start)
            for neighbor in graph[start]: 
                if neighbor not in visited: 
                    dfs(neighbor)

        dfs(0)
        return False if len(visited)!=n else True 