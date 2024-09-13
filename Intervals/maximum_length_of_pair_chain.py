class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        #Seems like an interval problem 
        #Wow constraint size is 1000 thats small 

        #I think sorting is a no brainer to start, the intervals are guaranteed
        #to be [0]<[1]

        #A chain is formed through NON overlapping intervals, so yeah we want to 
        #minimize ends 

        #We update end to be min of the end and then keep going? 

        #You do NOT have to use all the given intervals 

        #Okay got it we greedily want the shortest ends like I brainstormed so we 
        #will sort by end times 

        pairs.sort(key=lambda x:x[1])
        length=1 
        end=pairs[0][1]
        for i in range(1, len(pairs)): 
            if end<pairs[i][0]: 
                length+=1 
                end=pairs[i][1]
        return length 
        
        #My default is the 2 pointer, here since its literally just one chain, this 
        #is overkill, just use a for loop with one pointer^^
        pairs.sort(key=lambda x:x[1])
        i=0 
        while i<len(pairs): 
            length=1 
            j=i+1 
            end=pairs[i][1]
            while j<len(pairs): 
                if end<pairs[j][0]: 
                    length+=1 
                    end=pairs[j][1]
                j+=1 
            i=j
        return length 

        #Okay yeah got it, its one pass, it doesn't even consider other chains, its
        #always just the chain starting from the first interval 
        #Greedily get shortest end (thats why we sorted ends)
        
        #We ONLY need to consider the length of the chian starting form the first 
        #interval, this extends the interval with the shortest ending as far as 
        #possible which will always be the max length chain 
        