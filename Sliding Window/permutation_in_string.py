class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        #Permutation in s2 is a substring of s2, think SW
        #Permutation is just one to one freq matching? 

        from collections import Counter 
        onedict=Counter(s1)

        #We shrink when s2[r] not in s1/required
        #We don't shrink if s2[r] is in required, if we get matching then, return
        #true 
        #Othwise loop finishes and we return false 

        l=0 
        twodict=Counter()
        formed,required=0,len(onedict)
        for r in range(len(s2)): 
            if s2[r] in onedict:
                twodict[s2[r]]+=1 
                if twodict[s2[r]]==onedict[s2[r]]:
                    formed+=1 #(same logic, we've cmpleted one letter in the permu)
                while formed==required: 
                    if r-l+1==len(s1): 
                        return True 
                    if s2[l] in twodict: 
                        twodict[s2[l]]-=1 
                        if twodict[s2[l]]<onedict[s2[l]]: 
                            formed-=1 
                    l+=1 
        return False 

        
        
        #It just was much more inutitive for me for minimum window substring
        #to do while valid because that's when we update length/result and 
        #then to get smaller we shrink and still see if valid and can update
        
        #Committ this SW to memory: counter dict of smaller string, in the
        #for loop, first add s[r] to dict, if freq==other dict freq, formed+=1
        #then while loop for VALID, formed==required: first check condition/update
        #then decrement left dict freq, if that freq less than left freq of other dict
        #formed-=1, and then obv l+=1