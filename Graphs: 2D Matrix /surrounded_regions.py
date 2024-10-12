from collections import deque
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        #Should be similar to connected components/islands problems 
        #But needs additional check before being converted (needs to NOT be 
        #on the edge)
        #Recursive step, if (satisfies edge check), matrix[x][y]='X'

        #Well I gained some insight through the neetcode video, honestly this 
        #problem is just hard to understand its restraints lmao, could also 
        #seriously benifit from an example image of a much larger grid so you can 
        #clearly see the difference between border connected Os and non border 
        #connected Os

        #Any O on the border is not surrounded, that I know, but also, any O 
        #that is connected to a border O is not surrounded and that makes sense 
        #becuase its connected to an O that has no X border on the edge side 
        #So any O that is no part of the connected region of a border O is to be 
        #changed 

        #Visualize large scale grid, anything connected to border not to be changed
        #Everything else (think middle) is surrounded 

        #My steps: 
        #1. Iterate through the borders and for every O that's found, run a 
        #connected component dfs on it to find other connected Os, convert all 
        #such Os to Ts
        #2. Nested for loop to iterate through entire grid and convert all Os 
        #which now will be all valid to Xs
        #3. Grid is now Xs and Ts, one more nested for loop to change all Ts to Os

        def border_iterator(matrix):
            rows, cols=len(matrix), len(matrix[0])
            for j in range(cols): #first row 
                if matrix[0][j]=='O': 
                    connected_components(matrix, (0,j))
            for j in range(cols): #last row 
                if matrix[rows-1][j]=='O': 
                    connected_components(matrix, (rows-1, j))
            for i in range(1, rows-1): #first col minus first and last row cells
                if matrix[i][0]=='O': 
                    connected_components(matrix, (i, 0))
            for i in range(1, rows-1): #last col minus first and last row cells 
                if matrix[i][cols-1]=='O': 
                    connected_components(matrix, (i, cols-1))
            #Call connected_component for every O found on the border 


        def connected_components(matrix, start):
            #BFS
            rows, cols = len(matrix), len(matrix[0])
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            q = deque([start])
            
            # Mark the start position immediately to avoid reprocessing, saves time
            #efficiency 
            x, y = start
            matrix[x][y] = 'T'

            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == 'O':
                        q.append((nx, ny))
                        matrix[nx][ny] = 'T'  # Mark as visited when enqueued

        def connected_components(matrix, start): 
            #Recursive: 
            rows, cols=len(matrix), len(matrix[0])
            directions=[(-1,0), (1,0), (0,-1), (0,1)]
            x,y=start[0], start[1]

            if matrix[x][y]=='O': 
                matrix[x][y]='T'
                for dx,dy in directions: 
                    nx,ny=x+dx, y+dy
                    if 0<=nx<rows and 0<=ny<cols and matrix[nx][ny]=='O': 
                        connected_components(matrix, (nx,ny))
            #Find connected with start O and convert all to T 

        def connected_components(matrix, start): 
            #Iterative dfs
            rows, cols=len(matrix), len(matrix[0])
            directions=[(-1,0), (1,0), (0,-1), (0,1)]
            stack=[start]

            x,y=start 
            matrix[x][y]='T'
            while stack: 
                x,y=stack.pop()
                for dx,dy in directions: 
                    nx,ny=x+dx, y+dy
                    if 0<=nx<rows and 0<=ny<cols and matrix[nx][ny]=='O': 
                        stack.append((nx,ny))
                        matrix[nx][ny]='T'

        def Os_to_Xs(matrix): 
            for i in range(len(matrix)): 
                for j in range(len(matrix[0])): 
                    if matrix[i][j]=='O': 
                        matrix[i][j]='X'
        def Ts_to_Os(matrix): 
            for i in range(len(matrix)): 
                for j in range(len(matrix[0])): 
                    if matrix[i][j]=='T': 
                        matrix[i][j]='O'
        border_iterator(board)
        Os_to_Xs(board)
        Ts_to_Os(board)