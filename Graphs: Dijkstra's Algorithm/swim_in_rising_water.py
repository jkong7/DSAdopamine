class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols=len(grid), len(grid[0])
        directions=[(-1,0), (1,0), (0,-1), (0,1)]
        pq=[(grid[0][0],0,0)] #effort, x, y
        effort=[[float('inf')]*cols for _ in range(rows)] #Equivalent to distances dict
        effort[0][0]=grid[0][0]
        while pq: 
            cur_effort, x, y=heapq.heappop(pq)
            if x==rows-1 and y==cols-1: 
                return cur_effort 
            for dx,dy in directions: 
                nx,ny=x+dx, y+dy
                if 0<=nx<rows and 0<=ny<cols: 
        #Calculate "new distance" Equivalent to new_dist=cur_dist+weight:
                    new_effort=max(cur_effort, grid[nx][ny])
                    if new_effort<effort[nx][ny]: #Updating 
                        effort[nx][ny]=new_effort 
                        heapq.heappush(pq, (new_effort, nx, ny))
        return -1 
        #Twin problem with "path with minimum effort"
        #Only difference: "New effort" calculated as max of current and highest 
        #elevation encountered along the path to the neighboring cell 
        