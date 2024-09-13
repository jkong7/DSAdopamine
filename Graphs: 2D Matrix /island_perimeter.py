class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Exactly one island (one connected component)
        #Here are the cases: 
        #For each cell being processed: 
        #Neighboring one land cell: count+=3
        #Neighboring two land cells: count+=2 
        #Neighboring three land cells: count+=1 
        #Neighboring four land cells: count+=0 
        directions=[(-1,0), (1,0), (0,1), (0,-1)]
        rows, cols=len(grid), len(grid[0])

        self.perimeter=0 
        def grid_iterator(grid): 
            for i in range(rows): 
                for j in range(cols): 
                    if grid[i][j]==1: 
                        dfs(i, j)
        def dfs(x, y): 
            count=0 
            grid[x][y]=2 #Seen but still counts as land cell for perimeter calculatio
            for dx,dy in directions: 
                nx,ny=x+dx, y+dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] in [1,2]:
                    count+=1 
                    if grid[nx][ny]==1: 
                        dfs(nx,ny) 
            if count==0: 
                self.perimeter+=4
            elif count==1: 
                self.perimeter+=3
            elif count==2: 
                self.perimeter+=2
            elif count==3: 
                self.perimeter+=1
            elif count==4:
                self.perimeter+=0
        grid_iterator(grid)
        return self.perimeter
        directions=[(-1,0), (1,0), (0,1), (0,-1)]
        rows, cols=len(grid), len(grid[0])

        perimeter=0 
        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j]==1: 
                    count=4
                    for dx, dy in directions: 
                        nx,ny=i+dx,j+dy
                        if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1: 
                            count-=1
                    perimeter+=count
        return perimeter
