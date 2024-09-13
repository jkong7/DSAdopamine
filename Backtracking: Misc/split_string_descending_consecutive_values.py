class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #notice that s length is max 20, screams backtracking, and its a split
        #string problem, we consider all possibilities type problem, so 100% 
        #backtracking

        self.result=False
        def backtrack(start, maxx): 
            if start==len(s):
                self.result=True
            if maxx==None:
                for i in range(len(s)-1): 
                    backtrack(i+1, int(s[:i+1]))
            else: 
                for i in range(start, len(s)): 
                    if int(s[start:i+1])==maxx-1: 
                        backtrack(i+1, int(s[start:i+1]))
        backtrack(0, None)
        return self.result 


        #And then its for i in range(start, len(s)), and then the substring we 
        #examine each time recursively is s[start:i+1] and the new start is i+1
        #For this problem, we recursively pass in and update the maxx and we check
        #if our substring is maxx-1, and if it is that means we can continue. If we
        #can continue with this condition all the way to the end, it means we have
        #a valid path. Note that leading 0s are cut off to consider the actual val 
        #and conveniantly, int, which we must use to compare numbers anyways, cuts
        #them off for us. 

        #For the first iteration, we must handle it independetly because that tells
        #us how to init maxx. We pass in maxx as None and then if maxx is None 
        #which will only happen the first time, we call backtrack with the maxx
        #set as s[:i+1] to get the ball rolling. Also note that because it has 
        #to be AT LEAST 2 substrings, that initial calling MUST do i cannot go
        #all the way to the last elem of s or that's just one substring, the max 
        #it can go is the second to last elem. 
        
        #Note: The "is_valid" function here is int[s[start:i+1]]==maxx-1
        

