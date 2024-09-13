class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        from collections import Counter 
        if len(word1)!=len(word2): #O(1) 
            return False 
        word1dict=Counter(word1) #O(n) time and space 
        word2dict=Counter(word2) #O(n) time and space 
        return Counter(word1dict.values())==Counter(word2dict.values()) and \
        set(word1)==set(word2)
        #Time: O(n)
        #Space: O(n)

        #Two strings are operation 
        #equivalent if the FREQUENCIES of letters are the exact same. So use counter
        #to build frequency dicts of both words and then apply counter to the freq
        #of both dicts. This checks if the freqs have a one to one correspondance 
        #where order doesn't matter 
        #USEFUL: Counter()==Counter() checks if two iterable data structures have 
        #a one to one correspondance 

        #One additional check needed before all that^ is that no string has a letter
        #the other doesn't. Initially used a for loop for that but that is less eff
        #then comparing sets of the keys (using the dicts that we already built)
        #Next realization: This check is literally just set checking the og words
        #dummy 

        #Here's the one liner I've created myself: 
        return len(word1)==len(word2) and \
                set(word1)==set(word2) and \
                Counter(Counter(word1).values())==Counter(Counter(word2).values())
        #Note, use series of ands to mean that ALL statments must be true to return 
        #true. If any are not true, return false  
        
        #Three checks: 
        #1. Length must be same 
        #2. Characters used must be exact same 
        #3. Frequencies of letters must be same 

