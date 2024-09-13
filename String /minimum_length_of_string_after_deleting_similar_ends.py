class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Just remove as much as possible in one operation from left and right. At any 
        #moment, the left and right letters HAVE to be equal or else you stop right there

        left, right=0, len(s)-1 
        while left<right: 
            if s[left]!=s[right]: 
                return right-left+1 
            start=s[left]
            while left<len(s)-1 and s[left]==start: 
                left+=1
            while right>0 and s[right]==start: 
                right-=1 
        return 0 if left>right else 1 

