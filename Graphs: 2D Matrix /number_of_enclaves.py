class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #That's just the number of 1s that aren't connected components with a 
        #1 at the border 
        #Should be same problem as surrounded regions (but worded better lmao)
        #We can do a complementary counting, count number of 1s connected to 
        #border 1s and just turn those to 0s
        #Then just do a scan and number of 1s found is result 


        self.result=0 
        rows, cols=len(grid), len(grid[0])
        def border(grid): 
            for j in range(cols): #first row 
                if grid[0][j]==1: 
                    connected_components(grid, 0, j)
            for j in range(cols): #last row 
                if grid[rows-1][j]==1: 
                    connected_components(grid, rows-1, j)
            for i in range(1,rows-1): #first col 
                if grid[i][0]==1: 
                    connected_components(grid, i, 0)
            for i in range(1, rows-1): #last col 
                if grid[i][cols-1]==1: 
                    connected_components(grid, i, cols-1)

        def connected_components(grid, x, y): 
            directions=[(-1,0), (1,0), (0,-1), (0,1)]

            grid[x][y]=0 

            for dx,dy in directions: 
                nx,ny=x+dx,y+dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1: 
                    connected_components(grid, nx, ny)

        def ones_scan(grid):
            for i in range(rows): 
                for j in range(cols): 
                    if grid[i][j]==1: 
                        self.result+=1 
        border(grid)
        ones_scan(grid)
        return self.result