class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result=[]
        i=0 
        n=len(words) 
        while i<len(words): 
            started=words[i]
            ana=sorted(started)
            j=i+1  
            while j<n and sorted(words[j])==ana: 
                j+=1 
            result.append(started)
            i=j 
        return result 
        