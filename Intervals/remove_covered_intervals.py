class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        #Equivalent prompt: Find the number of intervals completely overlapped 
        #by another interval and subtract that from the number of intervals 

        #Greedy, i stays home, j fetches covered intervals compared to i, once 
        #property breaks, move i to right after last considered interval (no 
        #backtracking)

        #Need to sort intervals first (have to sort second/end value in decreasing
        #order too)
        intervals.sort(key=lambda x: (x[0], -x[1])) #O(n logn)
        i=0 
        n=len(intervals)
        covered=0 
        while i<n: #O(n)
            j=i+1
            while j<n and intervals[j][0]>=intervals[i][0] and intervals[j][1]<=intervals[i][1]:
                j+=1 
                covered+=1 
            i=j 
        return n-covered

        #Got to 32/34 testcases, realized that in case of start ties, we want 
        #the stay-at-home-i-interval to be the LARGER of the two intervals 
        #(longer end time). Always want the overlapper to be i: 
        #Same start time, bottom interval (same start time), needs to be considered
        #first so that i rests on that, otherwise that second overlapped interval
        #wouldn't be considered
        #.    ---------  ---
        #     ---------------
        #Therefore, need to sort end values in DECREASING ORDER so LARGER is 
        #considered first

        #Note: the while loop condition doesn't even need [j][0]>=[i][0] SINCE 
        #the intervals are already in start-sorted positions so the next interval
        #considered is guaranteed to have a start larger than the last. Thus to be
        #covered, only need to check that its end is before the previous end: 
        intervals.sort(key=lambda x: (x[0], -x[1])) #O(n logn)
        i=0 
        n=len(intervals)
        covered=0 
        while i<n: #O(n)
            j=i+1
            while j<n and intervals[j][1]<=intervals[i][1]:
                j+=1 
                covered+=1 
            i=j 
        return n-covered   
