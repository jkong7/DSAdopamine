class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Recursive dfs: 
        self.result=0 
        def call_on_matrix(matrix): 
            for i in range(len(matrix)): 
                for j in range(len(matrix[0])): 
                    if matrix[i][j]==1: 
                        dfs_connected_components(matrix, i, j)
                        self.result=max(self.result, dfs_connected_components(matrix, i, j))
        def dfs_connected_components(matrix, x, y): 
            directions=[(-1,0), (1,0), (0,-1), (0,1)]
            rows, cols=len(matrix), len(matrix[0])
            onecount=1 

            matrix[x][y]=0 #This is the the task at the current node visited by recursion
            for dx,dy in directions: 
                nx,ny=x+dy, y+dy
                if 0<=nx<rows and 0<=ny<cols and matrix[nx][ny]==1: 
                    onecount=1+dfs_connected_components(matrix, nx, ny)
                    #^Terminates current recursive step since if if statement not met, recursion call not made
            return onecount 
            call_on_matrix(grid)
            return self.result 


        #Should be a O(M*N) solution again (visit every cell)
        #Use same cell iterator and dfs/connected_components 
        #Keep a global count for result and a local count within the 
        #connected_components function and then take the max for result 

        self.result=0 
        def call_on_matrix(matrix): 
            for i in range(len(matrix)): 
                for j in range(len(matrix[0])):
                    if matrix[i][j]==1: 
                        dfs_connected_components(matrix, (i,j))

        def dfs_connected_components(matrix, start): 
            directions=[(-1,0), (1,0), (0,-1), (0,1)]
            rows, cols=len(matrix), len(matrix[0])
            one_count=0 #local count to be compared with global count 
            #don't need seen, modify matrix to 0s in place 
            stack=[start]
            while stack: 
                x,y=stack.pop() 
                if matrix[x][y]==1: 
                    matrix[x][y]=0 
                    one_count+=1
                    for dx, dy in directions: 
                        nx,ny=x+dx, y+dy
                        if 0<=nx<rows and 0<=ny<cols and matrix[nx][ny]==1: 
                            stack.append((nx,ny))
            self.result=max(self.result, one_count)
        call_on_matrix(grid)
        return self.result

         