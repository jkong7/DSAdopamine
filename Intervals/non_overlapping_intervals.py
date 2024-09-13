class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        #Compare adjacent intervals (sorted order)
        #IF they overlap, choose to remove the one with the longer end 

        #Greedily, at each comparison, remove the LONGER end 
        #interval and increment count by 1 (no backtracking, immediate increment + 
        #removal) 

        #Local optimization (remove longer end interval at each adjacent pair)

    #1. Removing intervals[i] Remove i, i goes to i+1 
        #---------------
      #     -------
    #2. Removing intervals[i+1], Remove i+1, i goes to i+2 
        #-------------
          #---------------
    #One if comparison each loop iteration, j always i+1 (1 adj pair compared each 
    #iteration)

      

        intervals.sort() #O(n logn)
        count=0 
        i=0 
        n=len(intervals)
        while i<n: #O(n) 
            j=i+1 
            while j<n and intervals[j][0]<intervals[i][1]: #Detect overlap 
                if intervals[j][1]<=intervals[i][1]: #Complete overlap 
                    count+=1 
                    i=j #Note i+=1 
                    j+=1 
                    #i goes +=1, j just needs same j=i+1 update 
                elif intervals[j][1]>intervals[i][1]: #Partial overlap 
                    count+=1 
                    j+=1 
                    #i stays at home and j goes to i+=2  
            i=j
        return count 