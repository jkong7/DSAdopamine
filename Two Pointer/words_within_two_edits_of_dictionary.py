class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """

        def edit(word1, word2): 
            one,two=0,0
            count=0 
            while one<len(word1): 
                if word1[one]!=word2[two]: 
                    count+=1 
                    if count>2: 
                        return False 
                one+=1 
                two+=1 
            return True 
    
        result=[]
        for i, word1 in enumerate(queries): 
            flag=False 
            for word2 in dictionary: 
                if edit(word1, word2) and not flag: 
                    result.append(word1)
                    flag=True 
        return result


