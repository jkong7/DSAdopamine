class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        #The algo should prob be one scan of s (some precomputation) and then a linear
        #scan of each words word 

        #Mhm actually well the words are only length 50 so you can prob just do a two
        #pointer on every single words with s
        n=len(s)
        def subs(word): 
            spoint, wpoint=0,0
            while spoint<n: 
                if s[spoint]==word[wpoint]: 
                    wpoint+=1 
                    if wpoint==len(word): 
                        return True 
                spoint+=1 
            return False 
        count=0 
        memo={}
        for word in words: 
            if word in memo: 
                if memo[word]: 
                    count+=1
                continue
            if subs(word): 
                count+=1 
            memo[word]=subs(word)
        return count 

            