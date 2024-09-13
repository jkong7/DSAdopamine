class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        #Maybe just brute force + keep track of max length and only go if length of cur
        #word is >= max length 
        #And also if dict word is longer than s dont go 

        def is_sub(word1, word2): 
            one,two=0,0
            while two<len(word2): 
                if word1[one]!=word2[two]: 
                    two+=1 
                else: 
                    one+=1 
                    two+=1 
                    if one==len(word1): 
                        return one 
            return False
        
        maxxlength, resword=0,''
        for word in dictionary: 
            if len(word)>len(s): 
                continue 
            elif len(word)==maxxlength: 
                if is_sub(word, s): 
                    if word<resword: 
                        resword=word 
            elif len(word)>maxxlength: 
                length=is_sub(word, s)
                if length: 
                    maxxlength, resword=length, word
        return resword

  
