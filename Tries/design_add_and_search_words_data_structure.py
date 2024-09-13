class TrieNode: 
    def __init__(self): 
        self.children={}
        self.end=False 

class WordDictionary(object):

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        current=self.root 
        for char in word: 
            if char not in current.children: 
                current.children[char]=TrieNode()
            current=current.children[char]
        current.end=True 
        #Same exact TrieNode set up + root and addWord function as in the normal trie 

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """


        #The function will have 2 functionalities, one if its just a regular char, 
        #we just do the regular iterative searching functionality, ie going to children
        #and returning false if children isn't there. Then at the end, if current is 
        #end of word, we return true. But it will also have a recursive functionality 
        #for when we see a '.' In this case, we will call dfs on ALL the CHILDREN of 
        #the current value as thats what the . means, it can take on ANY children value
        #so we pass in start+1 as the new start (indicates going down trie) as well 
        #as the child as the new root. The function returns a bool (postorder) and 
        #so if ANY child dfs call returned true, that means a word could be matched 

        def dfs(start, root): 
            current=root 
            for i in range(start, len(word)): 
                char=word[i]
                if char=='.': 
                    for child in current.children.values(): 
                        if dfs(i+1, child): 
                            return True 
                    return False 
                else: 
                    if char not in current.children: 
                        return False 
                    current=current.children[char]
            return current.end
        return dfs(0, self.root)
#char always is one level below current (we are trying to find a match from char to 
#a child of current, char starts at first letter, current starts at root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)