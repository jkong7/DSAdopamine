class Solution(object):
    def longestContinuousSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #A non continuous letter stops the previous subarray no matter what, there is 
        #no overlap, so can you just do two pointer home fetcher probably 

        nums=[]
        for char in s: 
            nums.append(ord(char)-ord('a'))
        n=len(nums) 
        i=0 
        maxx=0 
        while i<n: 
            prev=nums[i]
            j=i+1 
            while j<n and nums[j]==prev+1: 
                prev=nums[j]
                j+=1 
            maxx=max(maxx, j-i)
            i=j 
        return maxx 

        
        #I mean no need to make an extra array and loop to do all that, just do ord 
        #inside algo: 
        n=len(s) 
        i=0 
        maxx=0 
        while i<n: 
            prev=s[i]
            j=i+1 
            while j<n and ord(s[j])==ord(prev)+1: 
                prev=s[j]
                j+=1 
            maxx=max(maxx, j-i)
            i=j 
        return maxx 

        