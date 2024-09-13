class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0 
        count=0 
        n=len(s)
        while i<len(s): 
            j=i+1
            if s[i]=='1': 
                while j<n and s[j]=='1': 
                    j+=1 
                count+=(j-i)*(j-i+1)//2
            i=j 
        return count % (10**9+7)
    #HOME FETCHER!!!
