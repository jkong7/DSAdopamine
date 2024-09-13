from collections import deque 
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.result=0 
        def call_on_matrix(matrix): 
            for i in range(len(matrix)): 
                for j in range(len(matrix[0])): 
                    if matrix[i][j]=='1': 
                        self.result+=1 
                        connected_components(matrix, i, j)

        def connected_components(matrix, x, y): 
            directions=[(-1,0), (1,0), (0,-1), (0,1)]
            rows, cols=len(matrix), len(matrix[0])
            #current: 
            matrix[x][y]=0 
            for dx, dy in directions: 
                nx,ny=x+dx, y+dy
                if 0<=nx<rows and 0<=ny<cols and matrix[nx][ny]=='1': 
                    connected_components(matrix, nx, ny)
                #^Terminates current recursive step if if statement not met 
        call_on_matrix(grid)
        return self.result
        #^DFS recursion 

        self.result=0 
        def call_on_matrix(matrix): 
            # Using nested for-loops (left to right, top to bottom)
            for i in range(len(matrix)):        # Iterate over rows
                for j in range(len(matrix[0])): # Iterate over columns
                    if matrix[i][j]=='1':
                        self.result+=1 
                        connected_component(matrix, (i,j))

        def connected_component(matrix, start): 
            rows, cols=len(matrix), len(matrix[0])
            direction=[(-1,0), (1,0), (0,-1), (0,1)]

            q=deque([start])
            while q: 
                x,y=q.popleft()
                for dx,dy in direction: 
                    nx,ny=x+dx, y+dy
                    if 0<=nx<rows and 0<=ny<cols and matrix[nx][ny]=='1': 
                        matrix[nx][ny]='0'
                        q.append((nx,ny))
            #serves the purpose of filling seen up with connected components 
            #in the matrix iterate function, if a 1 is seen again, that means 
            #its a new connected component 
        call_on_matrix(grid)

        return self.result 
        #^
        #Don't need to use a seen set so saves some space, instead use an in-place
        #method-convert every 1 come across to a 0 and only trigger a dfs on 1s
        #Also bfs/dfs both work same here 


        self.result=0 
        self.seen=set()
        def call_on_matrix(matrix): 
            # Using nested for-loops (left to right, top to bottom)
            for i in range(len(matrix)):        # Iterate over rows
                for j in range(len(matrix[0])): # Iterate over columns
                    if (i,j) not in self.seen and matrix[i][j]=='1':
                        self.result+=1 
                        connected_component(matrix, (i,j))

        def connected_component(matrix, start): 
            rows, cols=len(matrix), len(matrix[0])
            direction=[(-1,0), (1,0), (0,-1), (0,1)]

            stack=[start]
            while stack: 
                x,y=stack.pop()
                if (x,y) not in self.seen: 
                    self.seen.add((x,y))
                for dx,dy in direction: 
                    nx,ny=x+dx, y+dy
                    if 0<=nx<rows and 0<=ny<cols and (nx,ny) not in self.seen and matrix[nx][ny]=='1': 
                        stack.append((nx,ny))
            #serves the purpose of filling seen up with connected components 
            #in the matrix iterate function, if a 1 is seen again, that means 
            #its a new connected component 
        call_on_matrix(grid)

        return self.result 

        #Every time we see a 1 that is not in visited, we increment count by 1 
        #The visited set should be universal 

        #Time complexity: 
        #Outer loop iterates through every cell O(M*N)
        #connected_component/dfs processes every cell exactly once O(M*N)
        #Note: Will be O(M*N) no matter if cells are 1 or 0
        #Total: O(M*N)

        #Space complexity: 
        #seen set can grow to number of cells O(M*N)
        #stack can grow to number of cells O(M*N) 
        #Note: Both of these occur if every cell is a '1' (worst case for space)
        #Total: O(M*N)
        