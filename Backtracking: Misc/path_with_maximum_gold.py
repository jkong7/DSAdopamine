class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Input size is super small, <15 (whole grid is 225 cells only) so points
        #to backtracking fosho 
        #And there are at most 25 cells containing gold, those are the only cells
        #we visit 

        #graph traversal 2D matrix plus backtracking to find all possible sums,

        #update self.largest with max 
        #Can't visit the same cell more than once so every time you recurse 
        #You can start and stop anywhere, stop anywhere is fine, self.largest 
        #sees all possible sums 

        #Start anywhere that HAS gold, I don't think it matters where you start, will
        #find all path sums anyways 

        #Pass in a visited set for recursion 

        directions=[(-1,0), (1,0), (0,-1), (0,1)]
        rows, cols=len(grid), len(grid[0])


        self.largest=0 
        def backtrack(x,y,visited, pathsum): 
            if pathsum>self.largest: 
                self.largest=pathsum #Can't return state here, have to keep searching
            for dx, dy in directions: #For loop over options space, backtracking
                nx,ny=x+dx,y+dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]!=0 and (nx,ny) not in visited: 
                    visited.add((nx,ny))
                    newpathsum=pathsum+grid[nx][ny]
                    backtrack(nx,ny,visited,newpathsum)
                    visited.remove((nx,ny))

        #Start from the max value?? OHHHH, you need to do this backtracking dfs 
        #on every unvisited node (within the dfs backtracking, mark visited nodes)
        #Last try: You call it at EVERY gold node with that starting gold val lmao
        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j]!=0:
                    backtrack(i,j,set([(i,j)]), grid[i][j])
        return self.largest

        #You call the dfs backtracking function at EVERY gold node with a global
        #largest variable that sees every possible path sum. For the backtracking
        #function, you just accumulate a pathsum and a visited set and then the 
        #recursive options loop is through the four directions here (nx,ny) must
        #not be in visited and must not be 0 to be visited 

        #Note: For sets passed in backtracking, easiest to backtrack with 
        #visited.add and then explicitly visited.remove after backtrack 
        
        #generally , as I have seen .
				#shortest path -> bfs
				#max sum of a path -> dfs + backtracking !

        