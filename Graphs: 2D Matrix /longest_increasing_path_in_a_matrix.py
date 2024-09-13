class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        directions=[(1,0), (-1,0), (0,-1), (0,1)]
        rows, cols=len(matrix), len(matrix[0])
        cache=[[-1]*cols for _ in range(rows)]


        def dfs(x, y): 
            if cache[x][y]!=-1: 
                return cache[x][y]
            maxlength=1 
            for dx, dy in directions: 
                nx,ny=x+dx,y+dy 
                if 0<=nx<rows and 0<=ny<cols and matrix[nx][ny]>matrix[x][y]: 
                    length=1+dfs(nx,ny)
                    maxlength=max(maxlength, length)
                cache[x][y]=maxlength 
            return maxlength 
        max_path=0 
        for i in range(rows): 
            for j in range(cols): 
                max_path=max(max_path, dfs(i,j))
        return max_path 

        #DFS+Memoization 
