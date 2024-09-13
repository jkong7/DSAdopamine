class Solution(object):
    def countAlternatingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #This one was is just get the length of the longest possible where you are at 
        #and then EVERYTHING in that length is valid. 
        #A lengtj 4 alternating is 4*5//2, similarly a length n alternating is 
        #n*(n+1)//2


        count=0 
        i=0 
        while i<len(nums): 
            prev=nums[i]
            j=i+1 
            while j<len(nums) and nums[j]!=prev:  
                prev=nums[j]
                j+=1 
            count+=(j-i+1)*(j-i)//2
            i=j 
        return count 


        #Nice concise solution, two pointer home fetcher goat 
        #Yeah no need for anything fancy sliding window or anything, well IG this is
        #kinda SW but not really, just moving pointers to where they need to be and 
        #then doing the count iterator which you just kinda build an intuition for 
        #doing a lot of SW/subararray count problems 
            