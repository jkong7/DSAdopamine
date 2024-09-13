class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t): 
            return False 
        tdict={}
        index=-1 
        for letter in t: 
            index+=1 
            if letter not in tdict: 
                if s[index] in tdict.values(): 
                    return False
                tdict[letter]=s[index]
            if letter in tdict: 
                if s[index]!=tdict[letter]: 
                    return False 
        return True 


     

        #if it's a new t letter, check to see if a previously mapped t-s value is 
        #at this current s index, one to one is broken. return false
        #if not, then create new valid t-s mapping
        #if it's an old t letter, s at current index must equal previously mapped t-s
        #value, if not then return false 
        #If no falses are hit after the for loop, return true

        #Note: Get in the habit of doing the O(1) length check before anything as it 
        #improves efficiency 

        #USEFUL: for c1, c2 in zip(s,t). Loops through both at same time
        #given that s and t are same length. Works w ANY iterable DS 


        #O(n) time (iterates through each string once O(n+n))
        #O(n) space (tdict)
        #Note: O(1) length check before carrying on so lengths are guaranteed to be =