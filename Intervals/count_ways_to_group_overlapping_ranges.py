class Solution(object):
    def countWays(self, intervals):
        """
        :type ranges: List[List[int]]
        :rtype: int
        """
        #This just a counting problem, how many "chunks" are there where a chunk is 
        #overlapping intervals

        #Yeah this just merge intervals logic for finding chunks 
        #And then its just 2^chunks 

        count=0 
        i=0 
        n=len(intervals) 
        intervals.sort()
        while i<n:
            count+=1 
            j=i+1 
            start, end=intervals[i][0],intervals[i][1]
            while j<n and intervals[j][0]<=end: 
                end=max(end, intervals[j][1])
                j+=1 
            i=j 
        return 2**count % (10**9+7)
        