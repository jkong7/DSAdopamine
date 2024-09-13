class TrieNode(): 
    def __init__(self): 
        self.children={}
        self.word=None 

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

    def getPrefix(self, word): 
        current=self.root
        for char in word: 
            if current.word: 
                return current.word
            if char not in current.children: 
                if current.word: 
                    return current.word 
                else: 
                    return None 
            current=current.children[char]
        return None  

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        trie=Trie()
        for word in dictionary: 
            trie.insert(word)
        words=sentence.split()
        result=[0]*len(words)
        for i,word in enumerate(words): 
            result[i]=trie.getPrefix(word) if trie.getPrefix(word) else words[i]
        return ' '.join(result)
