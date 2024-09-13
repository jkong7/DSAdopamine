class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def backtrack(path, summ, start): 
            if summ==n and len(path)==k: 
                result.append(path)
            if summ>n: 
                return 
            if len(path)>k: 
                return 
            for i in range(start, 10): #start will be init to 1, i+1 since no dupes
                newpath=path+[i] #Remember, immutable functionality, if use one 
                #mutable variable, need to explicitly path.pop() after recursive
                #backtrack call
                newsumm=summ+i #same here
                backtrack(newpath, newsumm, i+1) #1->(2,9)
            output=[]
            backtrack([], 0, 1)
            return output
            #Did over again fast for clarity
#Yes, your analysis is correct:

#The first for loop starts at 1.
#It goes 1 -> (2, 9).
#Once it returns, i shifts to 2 in the first for loop.
#Then it goes 2 -> (3, 9).
#In summary, each starting number leads to a recursive exploration of subsequent #numbers, ensuring no duplicates.




        #Small input size,

        #start, i+1 (no duplicates) for i in range(start, 10), start init to 1 
        #validation: len path==k and summ==n 

        def backtrack(path, summ, start): 
            if len(path)==k and summ==n: 
                output.append(path)
                return 
            if summ>n: 
                return 
            if len(path)>k: 
                return 
            for i in range(start, 10): #1-9 
                newpath=path+[i]
                newsumm=summ+i
                backtrack(newpath, newsumm, i+1)
        output=[]
        backtrack([], 0, 1)
        return output
        #I'm def seeing all the patterns together and being able to code them up 
        #no prob, eac number used at most once means i+1, if not then i. 
        #Here our validation is len(path) and summ, and then optimize the search 
        #by returning when either of the two exceed. 


        #Note for all problems: Can collapse into one line in the exploration f loop:
        def backtrack(path, summ, start): 
            if len(path)==k and summ==n: 
                output.append(path)
                return 
            if summ>n: 
                return 
            if len(path)>k: 
                return 
            for i in range(start, 10): #1-9 
                backtrack(path+[i], summ+i, i+1)
        output=[]
        backtrack([], 0, 1)
        return output


        