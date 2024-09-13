class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0 
        resultcount=0 
        sdict={}
        for r in range(len(s)): 
            if s[r] in sdict: 
                sdict[s[r]]+=1 
            else: 
                sdict[s[r]]=1 
            while l<=r and len(sdict)==3: 
                if sdict[s[l]]>1: 
                    sdict[s[l]]-=1 
                else: 
                    break 
                l+=1 
            if len(sdict)==3: 
                resultcount+=l+1
        return resultcount


        #The goal is to move the left until moving one further will result in it 
        #having only 2 letters
        #We shrink the window and increment l when we have a substring with the 
        #3 letters but note that the left letter appears more than once. 
        #In this case, we can move it and #of letters/len(sdict) remains 3 and we
        #are okay. 
        #Once the count of the left gets to only 1, the left pointer is where its
        #supposed to be at and we break out the while loop (not incrementing l again)

        #At this point, every substring from 0 to l and ending at r forms a valid 
        #substring so we add l+1 to the count 
