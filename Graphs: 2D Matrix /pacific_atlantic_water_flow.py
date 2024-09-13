class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        #Think dfs/bfs 
        #Pacific: x=0, y=anything        x=anything, y=0 
        #Atlantic: x=rows-1, y=anything       x=anything, y=cols-1 

        rows, cols=len(heights), len(heights[0])
        directions=[(-1,0), (1,0), (0,-1), (0,1)]

        pacific, atlantic=set(), set()

        def dfs(x, y, visited, prevheight): 
            if (x,y) not in visited:
                visited.add((x,y))
            for dx,dy in directions: 
                nx,ny=x+dx,y+dy 
                if 0<=nx<rows and 0<=ny<cols and (nx,ny) not in visited and heights[nx][ny]>=prevheight: 
                    dfs(nx,ny,visited,heights[nx][ny])

        for j in range(cols): 
            dfs(0,j,pacific, heights[0][j])
            dfs(rows-1, j, atlantic, heights[rows-1][j])
        for i in range(rows): 
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, cols-1, atlantic, heights[i][cols-1])

        result=[]
        for i in range(rows): 
            for j in range(cols): 
                if (i,j) in pacific and (i,j) in atlantic: 
                    result.append((i,j))
        return result 
