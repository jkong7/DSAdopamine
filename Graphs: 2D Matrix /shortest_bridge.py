from collections import deque 
class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Do a multi source BFS that starts with all the connected components of 
        #one island 
        #The moment one of those touches another 1, thats the minimum distance 

        rows, cols=len(grid), len(grid)
        directions=[(-1,0), (1,0), (0,-1), (0,1)]
        self.found=False
        q=deque()
        def initialize_first_island(grid): 
            for i in range(rows): 
                for j in range(cols): 
                    if grid[i][j]==1: 
                        dfs(i,j)
                        self.found=True
                        break
                if self.found==True: 
                    break 
        def dfs(x,y): 
            q.append((x,y))
            grid[x][y]=2
            for dx, dy in directions: 
                nx,ny=x+dx,y+dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1: 
                    dfs(nx,ny)
        initialize_first_island(grid)
        level=0
        while q: 
            level+=1 
            for _ in range(len(q)): 
                x,y=q.popleft()
                for dx, dy in directions: 
                    nx,ny=x+dx,y+dy
                    if 0<=nx<rows and 0<=ny<cols: 
                        if grid[nx][ny]==2: 
                            continue
                        elif grid[nx][ny]==0: 
                            q.append((nx,ny))
                            grid[nx][ny]=2
                        elif grid[nx][ny]==1:
                            return level-1  
        return -1 
       #Got it 
       #The ONLY thing i was forgetting was marking visited 0 cells to 2 (visited)
       #after. Just one line, literally everything else was spot on 
       #Three states: 0 unvisited, 2 visited, 1 goal (terminate and return)
       #O(MN) time and space, dfs/bfs O(MN) and dfs/bfs space O(MN)

