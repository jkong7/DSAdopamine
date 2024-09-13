class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Do the borders and call dfs on 0s and turn them to 1s 
        rows, cols=len(grid), len(grid[0])
        directions=[(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(x,y): 
            grid[x][y]=1 
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==0: 
                    dfs(nx,ny)

        for j in range(cols): 
            if grid[0][j]==0: 
                dfs(0,j)
        for j in range(cols): 
            if grid[rows-1][j]==0: 
                dfs(rows-1, j)
        for i in range(1, rows-1): 
            if grid[i][cols-1]==0: 
                dfs(i, cols-1)
        for i in range(1, rows-1): 
            if grid[i][0]==0: 
                dfs(i, 0)
        result=0 
        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j]==0: 
                    result+=1 
                    dfs(i,j)
        return result



        #Number of connected components of 0s that aren't part of a connected 
        #component of border 0s 
        #Count number of connected components from border 0s and turn those to 1s
        #Then grid iterate and do dfs on remaining 0s (turn them into 1s) and 
        #iterate result count by 1 each time you do that 

        self.result=0 
        rows, cols=len(grid), len(grid[0])
        def border(grid): 
            for j in range(cols): #first row 
                if grid[0][j]==0: 
                    connected_components(grid, 0, j)
            for j in range(cols): #last row 
                if grid[rows-1][j]==0: 
                    connected_components(grid, rows-1, j)
            for i in range(1,rows-1): #first col 
                if grid[i][0]==0: 
                    connected_components(grid, i, 0)
            for i in range(1, rows-1): #last col 
                if grid[i][cols-1]==0: 
                    connected_components(grid, i, cols-1)
        def connected_components(grid, x, y): 
            #Easiest, most concise: recursive dfs
            directions=[(-1,0), (1,0), (0,-1), (0,1)]
            grid[x][y]=1
            for dx,dy in directions: 
                nx,ny=x+dx,y+dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==0: 
                    connected_components(grid, nx, ny)

        def connected_components(grid, x, y): 
            #Just practice, iterative DFS
            directions=[(-1,0), (1,0), (0,-1), (0,1)]
            stack=[(x,y)]
            while stack: 
                x,y=stack.pop()
                grid[x][y]=1 
                for dx,dy in directions: 
                    nx,ny=x+dx,y+dy
                    if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==0:  
                        stack.append((nx,ny))
                        grid[x][y]=1 



        def grid_iterator_remaining_connected_components(grid): 
            for i in range(rows): 
                for j in range(cols): 
                    if grid[i][j]==0: 
                        connected_components(grid, i, j)
                        self.result+=1 
        border(grid)
        grid_iterator_remaining_connected_components(grid)
        return self.result 

