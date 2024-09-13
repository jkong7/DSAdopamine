from collections import deque 
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Plan: Follow same multi source BFS approach as 01 matrix 
        #In this case, distance is equivalent to minutes (minimum minutes covered
        #since we are using bfs on an unweighted graph)
        #Start with a q of rotton oranges (0s)
        #Mark fresh oranges inf (1s)
        #Keep a max counter every time you append a float inf to q to return 
        #at the end after q is empty 

        result=0 
        directions=[(-1,0), (1,0), (0,-1), (0,1)]
        rows, cols=len(grid), len(grid[0])
        q=deque()
        fresh=0 
        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j]==2: 
                    q.append((i,j))
                    grid[i][j]=0 
                elif grid[i][j]==1: 
                    grid[i][j]=float('inf')
                    fresh+=1 
        while q: 
            x,y=q.popleft()
            val=grid[x][y]
            for dx,dy in directions: 
                nx,ny=x+dx, y+dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==float('inf'): 
                    grid[nx][ny]=val+1 
                    result=max(result, grid[nx][ny])
                    fresh-=1 
                    q.append((nx,ny))
        return -1 if fresh!=0 else result 


#Can do it by doing level order (for loop of len q just like BT) and then
#after each level traversal, we can increment minutes count by 1 
        directions=[(-1,0), (1,0), (0,-1), (0,1)]
        rows, cols=len(grid), len(grid[0])
        q=deque()
        fresh=0 
        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j]==2: 
                    q.append((i,j))
                elif grid[i][j]==1: 
                    fresh+=1 
        if fresh==0: 
            return 0
        minutes=0 
        while q: 
            minutes+=1 
            for _ in range(len(q)):
                x,y=q.popleft()
                for dx,dy in directions: 
                    nx,ny=x+dx, y+dy
                    if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1: 
                        fresh-=1 
                        grid[nx][ny]=2 
                        q.append((nx,ny))

        return -1 if fresh!=0 else minutes-1

       