class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def bijection(word, pattern): 
            if len(word)!=len(pattern): 
                return False 
            ht={}
            for i,char in enumerate(word): 
                if char not in ht: 
                    if pattern[i] in ht.values(): 
                        return False 
                    else: 
                        ht[char]=pattern[i]
                else: 
                    if ht[char]!=pattern[i]: 
                        return False 
            return True 
        
        result=[]
        for w in words: 
            if bijection(w, pattern):  
                result.append(w)
        return result 
