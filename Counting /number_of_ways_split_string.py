class Solution(object):
    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD=10**9+7
        onecount=0 
        for char in s: 
            if char=='1':
                onecount+=1
        if onecount!=0 and onecount%3!=0: 
            return 0 
        if onecount==0: 
            n=len(s)-1
            return (n*(n-1)//2)%MOD
        ones=onecount//3 

        seen=0 
        result=1
        i=0 
        n=len(s) 
        while i<n: 
            needed=0 
            while i<n and needed<ones: 
                if s[i]=='1': 
                    needed+=1 
                    seen+=1 
                i+=1 
            start=i-1 
            while i<n and s[i]!='1' and seen<=2*ones: 
                i+=1 
            result=result*(i-start)%MOD
        return result

        #are there to insert two dividers into the 0s where the dividers have to be in 
        #between zeros. Theres len(s)-1 options and so its just that choose 2. 
        #For the main case, we get pointer to where it gets to ones needed and then find
        #the next one, and then that difference mutiplies to our result. The very last 
        #third though, it has to complete the string so theres only one way so once 
        #we get to that third (2/3 of onecount), we just multiply a 1 to the result 
        #(i is one greater than start) to stand for nothing new is added. 