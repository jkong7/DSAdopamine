from collections import defaultdict
class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        #Run a dfs to find connected components of grid 1 
        #Coordinates of a set in the map will be unique to that key 

        rows, cols=len(grid1), len(grid1[0])
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        island1=0 
        grid1map=set()
        def grid1_iterator(grid1): 
            for i in range(rows): 
                for j in range(cols): 
                    if grid1[i][j]==1: 
                        dfs1(grid1, i, j)

        def dfs1(grid, x, y): 
            grid1map.add((x,y))
            grid1[x][y]=0 
            for dx, dy in directions: 
                nx,ny=x+dx, y+dy
                if 0<=nx<rows and 0<=ny<cols and grid[x][y]==1: 
                    dfs1(grid, nx, ny)

        self.result=0 
        self.subisland=False 
        def grid2_iterator(grid2): 
            for i in range(rows): 
                for j in range(cols): 
                    if grid2[i][j]==1: 
                        self.subisland=True
                        if dfs2(grid2, i, j):  
                            self.result+=1 

        def dfs2(grid, x, y): 
            if (x,y) not in grid1map: 
                self.subisland=False  
            grid[x][y]=0
            for dx, dy in directions: 
                nx,ny=x+dx, y+dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1: 
                    dfs2(grid, nx, ny)
            return self.subisland

        grid1_iterator(grid1)
        grid2_iterator(grid2)
        return self.result 
        #Really cool logic with the subisland boolean 
        #and realizing that HT not needed but just a set and then checking if grid2
        #(x,y) is in that set. dfs2 returns the boolean which tells us whether 
        #subisland or not and it also does the seen functionaliy by setting 1s to 0s