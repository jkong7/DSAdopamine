class TrieNode(): 
    def __init__(self): 
        self.children={}
        self.word=None #Basically serves as .end AND gives you the whole word at once 
class Trie(): 
    def __init__(self): 
        self.root=TrieNode()

    def insert(self, word): 
        current=self.root 
        for char in word: 
            if char not in current.children: 
                current.children[char]=TrieNode()
            current=current.children[char]
        current.word=word

        
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        trie=Trie()
        for word in words: 
            trie.insert(word)

        def dfs(node): 
            if node.word: 
                if len(node.word)>self.length: 
                    self.length=len(node.word)
                    self.longestWord=node.word 
                elif len(node.word)==self.length: 
                    if node.word<self.longestWord: 
                        self.longestWord=node.word
            for child_node in node.children.values(): 
                if child_node.word: 
                    dfs(child_node)

        self.longestWord=''
        self.length=float('-inf')
        dfs(trie.root)
        return self.longestWord

        #yeah so make a trie with insert and we need a .word 
        #attribute to actually get the word, this is just the input of insert so its 
        #really to do, this also replaces .end. After that we just have to dfs on the 
        #trie where the base case is when the word ends which is if node.word, here we 
        #do the length comparisons and update our variables. To continue traversing we 
        #just go to the child_nodes which is in node.children.values(). However we can
        #only continue if if the child node is ALSO marking the end of a word which 
        #basically signifies it was an inserted full word in the og list, we can only
        #continue down current path if thats the case. 
