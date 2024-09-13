class Solution(object):
    def countOfPairs(self, n, x, y):
        """
        :type n: int
        :type x: int
        :type y: int
        :rtype: List[int]
        """
        #Will always come in pairs 

        from collections import defaultdict 
        from collections import deque 
        graph=defaultdict(list)
        for i in range(1, n): 
            graph[i].append(i+1)
            graph[i+1].append(i)
        graph[x].append(y)
        graph[y].append(x) 

        #Yeah do bfs from every node, count distances once from every node 
        #I think bfs and visited set implicitly handles the "getting there first", 
        #it will always get there in the shortest path, thats how unweighted shortest
        #path bfs works 
        
        def bfs(node, visited): 
            q=deque([(node, 0)])
            while q:  
                node, dist=q.popleft()
                if node not in visited and dist!=0: 
                    self.result[dist-1]+=1
                visited.add(node) 
                for neighbor in graph[node]: 
                    if neighbor not in visited: 
                        q.append((neighbor, dist+1))

        self.result=[0]*n #1,2,...n 
        for i in range(1, n+1): 
            bfs(i, set())
        return self.result 

        #But yeah, BFS on every node, bfs guarantees shortest paths, so every time
        #we get a distance, we add that distance to our min distance array. Doing it 
        #on every node and +=1 for every distance found ensures all unique pairs of 
        #houses are considered. (bfs on one house finds the shortest path between it
        #and all other houses) 

        #The part 2 of the problem is the exact same problem but the n input is 
        #10^5 instead of 100 here so my bfs from every node approach doesn't work 
        
