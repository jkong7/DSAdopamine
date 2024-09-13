from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #Multi source bfs starting with coords of treasure chests 
        #(values are already set to 0)
        #(land cells are already marked with inf, val+1 rolling dist
        #counter) grid[nx][ny]=val+1, q.append((nx,ny))
        #Multi source BFS 

        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        rows, cols=len(grid), len(grid[0])
        q=deque()
        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j]==0: 
                    q.append((i,j))
        while q: 
            x,y=q.popleft()
            val=grid[x][y]
            for dx, dy in directions: 
                nx,ny=x+dx,y+dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==2147483647:
                    grid[nx][ny]=val+1
                    q.append((nx,ny))