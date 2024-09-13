class TrieNode(): 
    def __init__(self): 
        self.children={}
        self.end=False 
class Trie(): 
    def __init__(self): 
        self.root=TrieNode()
    def insert(self, word): 
        current=self.root
        for char in word: 
            if char not in current.children: 
                current.children[char]=TrieNode()
            current=current.children[char]
        current.end=True 
    
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        #Matrix setup: 
        directions=[(-1,0), (1,0), (0,-1), (0,1)]
        rows, cols=len(board), len(board[0])
        #Begin by init our trie, insert all words into there 
        trie=Trie()
        for word in words: 
            trie.insert(word)
        #Just like in other matrix dfs problems, we need a visited functionality. We 
        #also need a result list, note that we don't want duplicate words in the result
        #so we can use a set and then convert it to a list at the end
        visited, result=set(),set()
        #Now for the backtracking/dfs function: 
        #Will have the x y coords, word path, and the current trie node 
        
        def dfs(x,y,node,path): 
            #Start by just adding to visited
            visited.add((x,y))
            #Now syncronize trie node to current board letter by accessing board[x][y]
            #of old node 
            currentnode=node.children[board[x][y]]
            #Add letter to our path (this inherently backtracks): 
            newpath=path+board[x][y]
            #Can potentially be a end word node and path/trie are syncronized so check:
            if currentnode.end: 
                result.add(newpath)
            #That's all we do, now just recursively explore
            for dx,dy in directions: 
                nx,ny=x+dx,y+dy
                #Needs to not be in visited AND HAS to be in children of current node letter (pruning occurs here!)
                if 0<=nx<rows and 0<=ny<cols and (nx,ny) not in visited and board[nx][ny] in currentnode.children: 
                    dfs(nx,ny,currentnode, newpath)
            #Remember to explicitly backtrack sets since they are mutable 
            visited.remove((x,y))
        
        #Now, call this function on every node that is in the children of the root which
        #is the equivalent of being a starting letter to any word in the bank 
        #We pass in our word-inserted trie's ROOT to the calls (always one behind rem)

        for i in range(rows): 
            for j in range(cols): 
                if board[i][j] in trie.root.children: 
                    dfs(i,j,trie.root, '')
        return list(result)


        
        #Trie will always be one behind the letter on the board, on each recursive, 
        #we move the pointer of the trie to now match the board letter. We do this 
        #so that when we now move to a next letter (directions), we can SEE IF THAT
        #NEW LETTER, i.e. board[nx][ny] is IN our trie nodes (remember one behind) 
        #children, if it IS, then we recurse, if it isn't, we just don't explore, thats
        #why the trie makes this so efficient, it effectively prunes the search space
        #as we only continue in directions that potentially form a valid word 

        #It is also used for end word validation. Before appending to result, we check
        #if the node is end AFTER we syncronize the trie node to our current boards 
        #letter. We simply use the O(1) bool check .end whereas we would otherwise have
        #to do an O(n) linear scan to see if our word is in words. The trie insert 
        #is designed to mark ends of words and so here, we conviniantly just use that! 

        #So two uses of the trie in this problem^^

        