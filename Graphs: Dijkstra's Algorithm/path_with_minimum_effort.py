import heapq

class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        rows, cols=len(heights), len(heights[0])
        directions=[(-1,0), (1,0), (0,-1), (0,1)]
        pq=[(0,0,0)] #effort, x, y
        effort=[[float('inf')]*cols for _ in range(rows)] #Equivalent to distances dict
        effort[0][0]=0 
        while pq: 
            cur_effort, x, y=heapq.heappop(pq)
            if x==rows-1 and y==cols-1: 
                return cur_effort 
            for dx,dy in directions: 
                nx,ny=x+dx, y+dy
                if 0<=nx<rows and 0<=ny<cols: 
        #Calculate "new distance" Equivalent to new_dist=cur_dist+weight:
                    new_effort=max(cur_effort, abs(heights[nx][ny]-heights[x][y]))
                    if new_effort<effort[nx][ny]: #Updating 
                        effort[nx][ny]=new_effort 
                        heapq.heappush(pq, (new_effort, nx, ny))
        return -1 