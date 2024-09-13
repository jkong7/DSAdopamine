from collections import deque 
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        val=image[sr][sc]
        directions=[(-1,0), (1,0), (0,1), (0,-1)]
        rows, cols=len(image), len(image[0])
        seen=set()
        q_or_stack=[(sr,sc)]
        while q_or_stack: 
            x,y=q_or_stack.pop()
            if (x,y) not in seen: 
                seen.add((x,y))
            image[x][y]=color
            for dx,dy in directions: 
                nx,ny=x+dx,y+dy
                if 0<=nx<rows and 0<=ny<cols and (nx,ny) not in seen and image[nx][ny]==val: 
                    q_or_stack.append((nx,ny))
        return image 

        def dfs(x,y): 
            if (x,y) not in seen: 
                seen.add((x,y))
            image[x][y]=color 
            for dx,dy in directions: 
                nx,ny=x+dx,y+dy
                if 0<=nx<rows and 0<=ny<cols and (nx,ny) not in seen and image[nx][ny]==val: 
                    dfs(nx,ny)
        dfs(sr,sc)
        return image 











        val=image[sr][sc]
        seen=set()
        def dfs(grid, color, x, y): 
            directions=[(-1,0), (1,0), (0,1), (0,-1)]
            rows, cols=len(image), len(image[0])

            stack=[(x,y)]
            while stack: 
                x,y=stack.pop()
                image[x][y]=color
                seen.add((x,y))
                for dx,dy in directions: 
                    nx,ny=x+dx,y+dy
                    if 0<=nx<rows and 0<=ny<cols and (nx,ny) not in seen and image[nx][ny]==val: 
                        stack.append((nx,ny))
        dfs(image, color, sr, sc)
        return image



        #Just a "connected components of a starting source" problem 
        seen=set()
        val=image[sr][sc]
        def connected_comp(image, x, y, color):
            directions=[(-1,0),(1,0),(0,-1),(0,1)]
            rows, cols=len(image), len(image[0])

            image[x][y]=color 
            seen.add((x,y))


            for dx,dy in directions: 
                nx,ny=x+dx,y+dy
                if 0<=nx<rows and 0<=ny<cols and (nx,ny) not in seen and image[nx][ny]==val: 
                    connected_comp(image, nx, ny, color)
        connected_comp(image, sr, sc, color)
        return image 