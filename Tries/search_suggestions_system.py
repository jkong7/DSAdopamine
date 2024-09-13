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
 

    def wordsInTrieThatStartsWithPrefix(self, prefix):
        result = []
        current = self.root
        
        for char in prefix:
            if char not in current.children:
                return result  
            current = current.children[char]
        
        self._collectAllWords(current, prefix, result)
        result.sort()
        return result[:3]

    def _collectAllWords(self, node, prefix, result):
        if len(result) >= 3:
            return
        if node.end:
            result.append(prefix)
        for char in sorted(node.children.keys()):
            if len(result) >= 3:
                return
            self._collectAllWords(node.children[char], prefix + char, result)


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        #Cool problem, in the Trie, create a method that returns a list of words
        #IN the trie that start with a given prefix. 
        #Then here, just first init a Trie by inserting all the words of products. 
        #Then, iterate through all prefixes of searchWord, for example m, mo, mou, etc
        #And call that method on each one and append its result (a list) to our final
        #result list. In that method, make sure to sort and then take only the first 3
        #which satisfies the three lexicographically minimum products. 

        productTrie = Trie()
        seen = set()
        for product in products:
            if product not in seen:  # Prevent duplicate insertion
                productTrie.insert(product)
                seen.add(product)

        result = []
        for i in range(len(searchWord)):
            result.append(productTrie.wordsInTrieThatStartsWithPrefix(searchWord[:i+1]))
        return result

        #^^Trie method 

