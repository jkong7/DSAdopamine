from collections import deque 
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows,cols=len(mat), len(mat[0])
        directions=[(-1,0), (1,0), (0,-1), (0,1)]
        q=deque()
        for i in range(rows): 
            for j in range(cols): 
                if mat[i][j]==0: 
                    q.append((i,j))
                else: 
                    mat[i][j]=float('inf')
        while q: 
            x,y=q.popleft()
            val=mat[x][y]
            
            for dx, dy in directions: 
                nx,ny=x+dx, y+dy
                if 0<=nx<rows and 0<=ny<cols and mat[nx][ny]==float('inf'): 
                    mat[nx][ny]=val+1 
                    q.append((nx,ny))
        return mat 
        #Again, main idea is that the moment a neighboring 1 is seen, that is the 
        #shortest path so do val+1 (where val is current node)
        #That 1 in the pq will be used to process its 1 neighbors which will 
        #accumulate distance (will always be shortest path due to BFS)



        #Instead, use a MULTI-SOURCE BFS approach 
        rows, cols=len(mat), len(mat[0])
        q=deque()
        def mat_iterator(matrix): 
            for i in range(rows): 
                for j in range(cols): 
                    if matrix[i][j]==0: 
                        q.append((i,j))
                    else: 
                        matrix[i][j]=float('inf')
        def multi_source_bfs(matrix): 
            directions=[(-1,0), (1,0), (0,-1), (0,1)]
            while q: 
                x,y=q.popleft()
                val=matrix[x][y]
                for dx, dy in directions: 
                    nx,ny=x+dx, y+dy
                    if 0<=nx<rows and 0<=ny<cols and (nx,ny) and matrix[nx][ny]==float('inf'): 
                        q.append((nx,ny))
                        matrix[nx][ny]=val+1 
        mat_iterator(mat)
        multi_source_bfs(mat)
        return mat 

        #When bfs encounters a float inf cell, that means its the first time 
        #that 1 cell has been encoutered, first time it reaches the cell is 
        #guaranteed to be shortest path due to bfs and so the distance is val+1 
        #A float inf encontered will be added to the q to process its neighbors 
        #but its own distance shoukd never be processed again since its update
        #distance is the shortest already (won't happen since only float inf cells
        #are processed). And this is also why seen set is unncessary, we update
        #float inf to val+1 as we go and we only q append float inf so thats 
        #a built in seen functionality 
        #Implemented myself after learning this multisource bfs approach 
        
#Multi-source BFS is a breadth-first search (BFS) algorithm that starts from 
#multiple sources simultaneously. Instead of starting BFS from a single node, 
#it enqueues multiple starting nodes (sources) and processes them in parallel.
# This is particularly useful for finding the shortest path from any of the multiple
#sources to other nodes in an unweighted graph.

#Yes, we use multi-source BFS in this problem because we need to find the shortest 
#path from each '1' to the nearest '0', and there are multiple '0's in the matrix. 
#Multi-source BFS efficiently finds the shortest distance to the nearest '0' for 
#all '1's simultaneously.




        #Initial solution: 
        #Grid scan, if its a 1, start a bfs there that counts how many times it has
        #to iterate until it reaches a 0

        #If its a 0, let it remain 0, if 1: update cell with distance 
        #Constraint: There is at least one 0, so don't have to worry about case 
        #whole board is 1s
        #Correct, but obviously slow because a bfs is being started at each 1, 
        #getting MLE
        rows, cols=len(mat), len(mat[0])
        def mat_iterator(matrix): 
            for i in range(rows): 
                for j in range(cols): 
                    if matrix[i][j]==1: 
                        matrix[i][j]=bfs(matrix, i, j)

        def bfs(matrix, x, y): 
            count=0 
            seen=set()
            directions=[(-1,0), (1,0), (0,-1), (0,1)]
            q=deque([(x,y)])
            while q: 
                count+=1 
                q.popleft()
                seen.add((x,y))
                for dx,dy in directions: 
                    nx,ny=x+dx, y+dy
                    if 0<=nx<rows and 0<=ny<cols and (nx,ny) not in seen: 
                        q.append((nx,ny))
                        if mat[nx][ny]==0: 
                            return count 

        mat_iterator(mat)
        return mat 




# Level-Order Traversal:
# BFS explores nodes level by level, meaning it first explores all nodes at the current
# "depth" (distance) before moving on to nodes at the next depth level. This guarantees
# that the first time BFS reaches a node, it does so via the shortest path.

# Unweighted Grids:
# In a 2D matrix where all moves have the same "weight" (i.e., moving from one cell
# to an adjacent cell always takes the same effort or cost), BFS ensures that the
# shortest path is found efficiently. Since all edge weights are equal, BFS ensures
# that the shortest path is found as soon as a node is visited.

# Shortest Path Guarantee:
# When BFS visits a node for the first time, it guarantees that it is the shortest path
# to that node from the starting node. Any subsequent visit to the same node would
# necessarily involve a longer path.

#Standard BFS to find shortest path (start coord to end coord): 
from collections import deque

def shortestPath(grid, start, end):
    """
    Finds the shortest path in a 2D grid from start to end.
    
    :param grid: List[List[int]] - The 2D grid
    :param start: Tuple[int, int] - The starting coordinates (row, col)
    :param end: Tuple[int, int] - The destination coordinates (row, col)
    :return: int - The length of the shortest path, or -1 if no path exists
    """
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right
    
    # BFS setup
    q = deque([start])
    visited = set([start])
    distance = 0
    
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            
            # Check if we have reached the destination
            if (x, y) == end:
                return distance
            
            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and (nx, ny) not in visited:
                    q.append((nx, ny))
                    visited.add((nx, ny))
        
        # Increment distance after exploring all nodes at the current distance
        distance += 1
    
    # If the destination is not reached
    return -1