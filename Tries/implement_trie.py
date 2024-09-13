class TrieNode: 
    def __init__(self): 
        self.children={}
        self.endOfWord=False 
        #Connections/children are represented using a hashmap and we also use
        # a boolean to represent the end of a word 

class Trie(object):

    def __init__(self):
        self.root=TrieNode()
        #We just need to init our root node as a TrieNode
        
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current=self.root 
        for char in word: 
            if char not in current.children: 
                current.children[char]=TrieNode()
            current=current.children[char]
        current.endOfWord=True 
        #Starts at the root and iterates through every letter in word, for every
        #letter, if it exists in the current nodes/letters children, nothing 
        #happens and current pointer simply moves to that letter now. However, 
        #if it DOESN'T exist in a nodes children, the current nodes char children
        #will be set to a new TrieNode and thats how we insert a deviation from
        #the shared prefix, also here current is moved to this new node and new
        #nodes are created as needed.
        #On the last letter, the word is now complete so we have to mark that node
        #as endOfWord True 

        #Ex: apple is the trie, if we insert append, it will go down to a then p
        #then p, and now e is not in ps children so a e node is created as a child
        #of p, then n and d follow this. 
    

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current=self.root 
        for char in word: 
            if char not in current.children: 
                return False 
            current=current.children[char]
        return current.endOfWord 
        #Nice nice, after learning insert, implemented this one fully myself 
        #Same logic, try to follow down the children of current node for as long
        #as possible, if at any moment a char is not in the current nodes children, 
        #the word is not there and return false
        #At the end of the loop, we need to check if the current node (last letter)
        #is marked as endofword and only then do we return true, else false 

        
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current=self.root 
        for char in prefix: 
            if char not in current.children: 
                return False 
            current=current.children[char]
        return True 
        #And this one too, same exact thing as search but here we are looking for
        #prefix to be in there so still same (if not in children, return false) but
        #now at the end, we dont need to check if it is endofword. Just, if it 
        #reached the end, we know the prefix is in there so we can return true

        #Note: All three methods are extremely similar! Just starting a current
        #pointer at the root and then try to follow to its children as much as 
        #possible, if break: do something: insert TrieNode, return false. Then
        #at the end, do somethimng: mark end of word, return True/false 
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)