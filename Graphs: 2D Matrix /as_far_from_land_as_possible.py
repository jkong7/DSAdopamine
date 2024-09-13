class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Multi source bfs with all the 1s in the deque initially and then set 
        #the 0s to temp such as float(inf)

        #Then just mark the vals with val+1 and use variable to keep track of max 

        directions=[(1,0), (-1,0), (0,-1), (0,1)]
        rows, cols=len(grid), len(grid[0])
        from collections import deque 
        q=deque()
        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j]==1: 
                    q.append((i,j))
                    grid[i][j]=0 #Dist vals init to 0 in this pass too, makes it easy
                else: 
                    grid[i][j]=float('inf')
        #Only visit if its float(inf) which means visited, else the moment we get
        #to a water cell, thats its distance to nearest land cell is set in stone 
        #b/c of BFS
        largest=float('-inf')
        while q: 
            x,y=q.popleft()
            val=grid[x][y]
            for dx,dy in directions: 
                nx,ny=x+dx,y+dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==float('inf'): 
                    grid[nx][ny]=val+1 
                    if val+1>largest: 
                        largest=val+1
                    q.append((nx,ny))
        return -1 if largest==float('-inf') else largest 