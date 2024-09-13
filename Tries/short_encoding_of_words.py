class TrieNode(): 
    def __init__(self): 
        self.children={}


class Trie(): 
    def __init__(self): 
        self.root=TrieNode()
        self.ends=[]

    def insert(self, word): 
        current=self.root 
        for char in word: 
            if char not in current.children: 
                current.children[char]=TrieNode()
            current=current.children[char]
        self.ends.append([current, len(word)+1])


class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        #Basically group words into their longest word such that all the words are 
        #substrings of that word, that provides the min length added to s (len long word
        #+1)

        #Ah this is just trie inserting, "grouped" words will only show up as the 
        #total long word in the trie

        #So you just need to count the length of the ending words in the trie 

        words=list(set(words))
        words.sort(key=len, reverse=True)
        trie=Trie()
        for word in words: 
            trie.insert(word[::-1])
        return sum([depth for node,depth in trie.ends if len(node.children)==0])

