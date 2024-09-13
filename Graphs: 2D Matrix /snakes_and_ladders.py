from collections import deque 
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        #Shortest path problem 
        #Unweighted (all 1-6 moves cost the same) 
        #2D matrix traversal
        #Should automatically think BFS 

        #Rolling distances BFS method (tag each cell with its bfs shortest distance,
        #once gets to destination, return the tag)
        length=len(board)
        board.reverse()
        seen=set()
        def intToPos(square): 
            r=(square-1)//length
            c=(square-1)%length
            if r%2: 
                c=length-1-c
            return [r,c]
        q=deque([(1,0)]) #Square, number of moves
        while q: 
            square, moves=q.popleft()
            for i in range(1,7): 
                new_square=square+i 
                r,c=intToPos(new_square)
                if board[r][c]!=-1: 
                    new_square=board[r][c]
                if new_square==length*length: 
                    return moves+1 
                if new_square not in seen: 
                    seen.add(new_square)
                    q.append((new_square, moves+1))
        return -1 
