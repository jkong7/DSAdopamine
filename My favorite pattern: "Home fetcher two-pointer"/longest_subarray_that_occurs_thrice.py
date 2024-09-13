class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict 
        ht=defaultdict(int) 
        i=0 
        n=len(s) 
        while i<n: 
            j=i+1 
            start=s[i]
            while j<n and s[j]==start: 
                j+=1 
            increment=j-i 
            for i in range(1, j-i+1):
                ht[i*start]+=increment 
                increment-=1 
            i=j 
        maxx=-1 
        for key,value in ht.items(): 
            if value>=3: 
                maxx=max(maxx, len(key))
        return maxx
        #Home fetcher to use math to count occurences of substring lengths of a 
        #consecutive component like "aaaaa". Store these in ht and find the max length
        #key where value>=3 after looping through string. 