class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        #So should be similar to permutations 
        #Validation check: len path ==k 
        #newpath=path+[options[i]]
        #How to limit options?
        #start, n 
        #permutations was everything except current 

        #seems like subsets but with the length validation check 

        def backtrack(path, start):
            if len(path)==k: 
                output.append(path)
                return 
            for i in range(start, n+1):  #1-4
                newpath=path+[i]
                backtrack(newpath, i+1)
        output=[]
        backtrack([], 1)
        return output

 
        