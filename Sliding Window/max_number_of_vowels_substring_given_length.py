class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        
         
        vowels=['a', 'e', 'i', 'o', 'u']
        vowelcount=0 
        for i in range(k): 
            if s[i] in vowels: 
                vowelcount+=1 
        result=vowelcount 
        for r in range(k, len(s)): 
            if s[r-k] in vowels: 
                vowelcount-=1 
            if s[r] in vowels: 
                vowelcount+=1 
            result=max(result, vowelcount)
            print(result)
        return result 

        #Fixed size sliding window problem 

        #Start with the first k elements and its vowelcount. Also set result equal
        #to vowelcount. Considerations for a higher result are made each time
        #the left end is cut off and the right is added on. Same basic fixed SW 
        #logic: r goes from k to end of array, left end is r-k (or l; l=0; l+=1).
        #r pointer moves no matter what, vowelcount updated based on if the left
        #and right ends are vowels 

     