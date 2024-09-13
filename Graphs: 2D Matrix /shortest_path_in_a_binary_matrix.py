from collections import deque 
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #One source so single source bfs
        #q initialized with start 
        #Do with level and then increment count 
        #8 directionally counted 
        #q append if grid[nx][ny]==0 
        #Stop and return count if x==n-1 and y==n-1 
        #Can do an updating cells count or global counter method, I did both: 
				#O(M*N)

				#Level by level bfs with level counter 
        level=0 
        directions=[(-1,0), (1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        rows, cols=len(grid), len(grid[0])
        if grid[0][0]==1 or grid[rows-1][cols-1]==1: #return -1 edge cases 
            return -1 
        q=deque([(0,0)])

        while q: 
            level+=1 
            for _ in range(len(q)): 
                x,y=q.popleft()
                for dx,dy in directions: 
                    if x==rows-1 and y==cols-1: 
                        return level 
                    nx,ny=x+dx,y+dy
                    if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==0: 
                        grid[nx][ny]=1 #Mark as visited 
                        q.append((nx,ny))
        return -1 #Necessary placeholder (will never execute)

        #Got it pretty fast (process level by level and once that level is proc
        #using for loop over len(q) just like BT, increment count by 1)



        #BFS with rolling distance counter:
        directions=[(-1,0), (1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        rows, cols=len(grid), len(grid[0])
        if grid[0][0]==1 or grid[rows-1][cols-1]==1: #return -1 edge cases 
            return -1 
        q=deque([(0,0)])
        while q: 
            x,y=q.popleft()
            val=grid[x][y]
            if x==rows-1 and y==cols-1: 
                return grid[x][y]+1
            for dx, dy in directions: 
                nx,ny=x+dx,y+dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==0: 
                    grid[nx][ny]=val+1 #Update value to rolling distance counter 
                    q.append((nx,ny))
        return -1
        #Got it both ways 
        
        #Signs to obv use bfs: Shortest path, unweighted, traverse to adj 
        #nodes (2D matrix, can move 8 directionally to adj), follows typical
        #level order behavior 
