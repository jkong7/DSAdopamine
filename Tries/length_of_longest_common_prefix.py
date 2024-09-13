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

    def get_length(self, word): 
        length=0 
        current=self.root
        for char in word: 
            if char not in current.children: 
                return length 
            else: 
                current=current.children[char]
                length+=1 
        return length 

class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        trie=Trie()
        arr1=[str(x) for x in arr1]
        for string in arr1: 
            trie.insert(string) 
        
        maxx=0 
        arr2=[str(x) for x in arr2]
        for string in arr2: 
            maxx=max(maxx, trie.get_length(string))
        return maxx 




        