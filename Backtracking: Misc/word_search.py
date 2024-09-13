class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        rows, cols=len(board), len(board[0])
        directions=[(1,0),(-1,0),(0,-1),(0,1)]

        def dfs(x,y,index): 
            if index==len(word): 
                return True 
            temp=board[x][y]
            board[x][y]='Temp'
            for dx,dy in directions: 
                nx,ny=x+dx,y+dy
                if 0<=nx<rows and 0<=ny<cols and board[nx][ny]==word[index]: 
                    if dfs(nx,ny,index+1): 
                        return True 
            board[x][y]=temp
            return False 

        #Marks as visited/temp while going down the valid dfs and then when its not, 
        #goes back to the call/cell where it was last valid and rewinds/resets 
        #all cells along the way 
        

        for i in range(rows): 
            for j in range(cols): 
                if board[i][j]==word[0]: 
                    if dfs(i,j,1): 
                        return True 
        return False
        #Did again fast for clarity 


        #4 direc connected 
        #seen set 
        #keep a next letter in word var and check if board[nx][ny]==var

        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        rows, cols=len(board), len(board[0])


        def backtrack(x,y,index): 
            if index==len(word): 
                return True 
            temp=board[x][y]
            board[x][y]='Visited'
            for dx,dy in directions: 
                nx,ny=x+dx,y+dy
                if 0<=nx<rows and 0<=ny<cols and board[nx][ny]==word[index]: 
                    if backtrack(nx,ny,index+1): 
                        return True
            board[x][y]=temp
            return False
            

        for i in range(rows): 
            for j in range(cols): 
                if board[i][j]==word[0]: 
                    if backtrack(i,j, 1): #coordinate, path 
                        return True 
        return False

        #If a path doesn't workout, the main double for loop can still use those 
        #original characters (restoration allows this)
        #But it also serves as a visited functionality for the backtracking 
        #function, prevents revisiting the same cell within the same recursive 
        #path 

        