class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """ 

        #Greedy: Chooses the narrowist possible interval that overlaps with the 
        #current and subsequent balloons to minimize the number of arrows needed,
        #does this immediately/makes the best local decision at each step without 
        #considering future consequences
        #Each choice is made based on the current situation alone, aiming to achieve
        #the best immediate result. "Local optimization ->global optimization"

        #Note: Instead of merging and increasing the width of the intervals, 
        #here we merge and shrink the intervals.

        points.sort() #O(n logn)
        i=0 
        count=0 
        n=len(points)
        while i<n: #O(n) 
            left=points[i][0]
            right=points[i][1]
            j=i+1 
            while j<n and left<=points[j][0]<=right: 
                left=max(left, points[j][0])
                right=min(right, points[j][1])
                j+=1 
            count+=1 
            i=j 
        return count 


        #Overlapping interval gets shot 
        #Minimum number of intervals to remove so that 
        #Finding the sweet spot of an interval such that that point overlaps 
        #with as many future intervals as possible 

        #Def sort by start time 

        #Greedy: Always choose the furthest possible end of an adjacent pair and 
        #then use that to compare to the next interval(s), then move i to right
        #after all compared intervals (no backtracking)
        #If complete overlap: Furthest possible end is j[1]
        #If partial overlap: Furthest possible end is i[1]


        points.sort()
        i=0 
        n=len(points)
        count=0 
        while i<n: 
            j=i+1 
            popper=None 
            if j<n and points[j][0]<=points[i][1]: #Detect overlap 
                if points[j][1]<=points[i][1]: #Complete overlap 
                    popper=points[j][1]
                elif points[j][1]>points[i][1]: #Partial overlap 
                    popper=points[i][1]
                while j<n and points[j][0]<=popper: #Move j as far as possible 
                    j+=1 
                count+=1 #All intervals in popper range accumulates to one arrow
            else: 
                count+=1 #If no overlap, one arrow one balloon 
            i=j #i always jumps to new home j at the end of comparisons 
        return count 
    
    #Popper will have two ends

