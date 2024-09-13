class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        #Mark down the indices of the FIRST uppercase letter and then compare lowercase
        #to them, if index of lowercase>first uppercase, its invalid, put it in a set, 
        #we only do comparisons if the letter is lowercase. 
        #Return len(ht)-len(invalid)

        from collections import Counter 
        count=Counter(word) 
        special=set()
        for char in word: 
            if char.islower() and char.upper() in count: 
                special.add(char)
        n=len(special)

        ht={}
        for i,char in enumerate(word): 
            if char.isupper() and char.lower() not in ht: 
                ht[char.lower()]=i
        
        invalid=set()
        for i,char in enumerate(word): 
            if char.islower() and char in special and char not in invalid: 
                if i>ht[char.lower()]: 
                    invalid.add(char.lower())
        return n-len(invalid)


        