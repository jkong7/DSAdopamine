from collections import deque 
class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        #Multi source bfs by q appending all the empty cells AT THE BORDER 
        #result=min(result, )
        #Probably not multi source dfs actually since there is only one person 
        #BFS starting from the person (entrance), do a level by level count 
        #and the FIRST empty border cell you see return level 


        directions=[(-1,0), (1,0), (0,1), (0,-1)]
        rows, cols=len(maze), len(maze[0])
        q=deque([(entrance[0], entrance[1])])
        maze[entrance[0]][entrance[1]]='+'
        level=0 
        while q: 
            level+=1 
            for _ in range(len(q)): 
                x,y=q.popleft()
                if x==rows-1 or y==cols-1 or x==0 or y==0: 
                    if x==entrance[0] and y==entrance[1]: 
                        pass
                    else: 
                        return level-1 
                for dx,dy in directions: 
                    nx,ny=x+dx,y+dy 
                    if 0<=nx<rows and 0<=ny<cols and (nx,ny) and maze[nx][ny]=='.': 
                        q.append((nx,ny))
                        maze[nx][ny]='+'
        return -1 
         
        #Single source BFS shortest path problem 
        #Mostly got it 
        #Level counter (for loop over len q), return it when our x y is on a border
        #cell 
        #Seen functionality, just need to mark visited cells with '+'. Do it 
        #BEFORE added to the q. Thus, also need to mark entrance cell with a +
        #as the code won't mark that, only neighbors and future neighbors 

    #Cells should be marked as visited **before** they are appended to 
    #the queue to avoid reprocessing and ensure they are not added to the 
    #queue multiple times. This prevents infinite loops and ensures the BFS 
    #runs correctly.