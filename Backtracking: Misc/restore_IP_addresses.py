class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """ 
        def backtrack(path, start, dotcount): 
            def is_valid(string): 
                return len(string)==1 or (string[0]!='0' and int(string)<=255)

            if dotcount==3: 
                if start<len(s) and is_valid(s[start:]): 
                    output.append(path+s[start:])
                return 
            for i in range(start, min(start+3, len(s))): 
                if is_valid(s[start:i+1]):
                    newpath=path+s[start:i+1]+'.'
                    backtrack(newpath, start+len(s[start:i+1]), dotcount+1)
        output=[]
        backtrack('', 0, 0)
        return output


        #Will go through all 3-or-less-in-between dot placements (all will be
        #valid and then at the end of the combo with 3 dots, will be checked
        #for validity)
        #^Beats 99.3% runtime 
        #Did it over again fast for clarity 



        #Forgot that no leading zeros condition
        #Just design an is_valid function, no leading zeros and must be 
        #less than 255 (or len string is 1)
        #need to do is_valid (multi checker) not just for the end 
        #s[start:] but also for all new substring appends to newpath
        #Remember to always have the return statement at the end of the 
        #validation checker 

        def is_valid(string): 
            return len(string)==1 or (string[0]!='0' and int(string)<=255)

        def backtrack(path, start, dotcount):
            if dotcount==3:
                if start<len(s) and is_valid(s[start:]):
                    output.append(path+s[start:])
                return 
            for i in range(start, min(start+3,len(s))):
                if is_valid(s[start:i+1]):
                    newpath=path+s[start:i+1]+'.'
                    backtrack(newpath, start+len(s[start:i+1]), dotcount+1)
        output=[]
        backtrack('', 0, 0)
        return output 

        #Mostly got it, had the right ideas with start:i+1 and the end checker
        #Forgot about the leading zeroes check. Got the dotcount==3 and 
        #coded up is_valid and correctly placed it. 
        #Really really like this problem 

        