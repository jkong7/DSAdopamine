class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        #Already sorted in ascending order by start 

        #Given NON OVERLAPPING intervals 

        #Basic empty input case:

        if not intervals: 
            return [newInterval]
        #1. FIRST CASE: NO OVERLAP

        n=len(intervals) 

        if newInterval[1]<intervals[0][0]: #Left no overlap 
            intervals.insert(0, newInterval)
            return intervals 
        
        if newInterval[0]>intervals[-1][1]: #Right no overlap 
            intervals.append(newInterval)
            return intervals 
        
        result=[] #Middle no overlap 
        i=0 
        while i<n: 
            if newInterval[0]>intervals[i][1] and newInterval[1]<intervals[i+1][0]:
                result.append(intervals[i])
                result.append(newInterval)
                while i+1<n: 
                    result.append(intervals[i+1])
                    i+=1 
                return result 
            else: 
                result.append(intervals[i])
                i+=1 


        #2. SECOND CASE: COMPLETE OVERLAP 

        #2.1: New interval completely overlaps original interval (inclusive)
        result=[]
        i=0 
        while i<n: 
            if newInterval[0]<=intervals[i][0] and newInterval[1]>=intervals[i][1]:
                start, end=newInterval[0], newInterval[1]
                l=i-1
                r=i+1 
                while l>=0 and start<=intervals[l][1]: 
                    start=min(start, intervals[l][0])
                    l-=1 
                while r<=n-1 and end>=intervals[r][0]: 
                    end=max(end, intervals[r][1])
                    r+=1 
                for left in range(l+1): 
                    result.append(intervals[left])
                result.append([start, end])
                for right in range(r, n): 
                    result.append(intervals[right])
                return result 
        #2.2 Original interval completely overlaps new interval (not inclusive)
        #Just gets overshadowed by original, just return original intervals array
            elif newInterval[0]>intervals[i][0] and newInterval[1]<intervals[i][1]: 
                return intervals 
            else: 
                i+=1 
                
        #3. THIRD CASE: PARTIAL OVERLAP 
        result=[]
        i=0 
        while i<n: 
            if newInterval[1]>=intervals[i][0] and newInterval[0]<intervals[i][0]: #Left side leaning/exploring 
                start=min(newInterval[0], intervals[i][0])
                end=max(newInterval[1], intervals[i][1])
                l=i-1 
                r=i+1 
                while l>=0 and start<=intervals[l][1]:
                    start=min(start, intervals[l][0])
                    l-=1
                for left in range(l+1): 
                    result.append(intervals[left])
                result.append([start, end])
                for right in range(r, n): 
                    result.append(intervals[right])
                return result 
            elif newInterval[0] <= intervals[i][1] and newInterval[1] >= intervals[i][0]: #Right side leaning/exploring 
                start=min(newInterval[0], intervals[i][0])
                end=max(newInterval[1], intervals[i][1])
                l=i-1 
                r=i+1 
                while r<=n-1 and end>=intervals[r][0]: 
                    end=max(end, intervals[r][1])
                    r+=1 
                for left in range(l+1): 
                    result.append(intervals[left])
                result.append([start, end])
                for right in range(r, n): 
                    result.append(intervals[right])
                return result 
            else: 
                i+=1 

        #Got the two example cases, ill hunt for more cases now  

        #1. New intervals before all intervals X
        #2. New interval after all intervals X
        #3. New interval between two non overlapping intervals X
        #4. New Interval Completely Overlapping an Existing Interval X
        #5. New Interval Completely Overlapped by an Existing Interval X
        #6. New Interval Partially Overlapping with One Interval X
        #7. New Interval Partially Overlapping with Multiple Intervals X
        #8. New Interval covering multiple intervals X
        #9. Empty list of intervals X
        #10. Exact overlap with an existing interval X
        #11. Touching intervals: X

        #intervals = [[1, 2], [5, 6]], newInterval = [2, 5]
        #Output: [[1,5], [5,6]]     should be [1,6]


        #intervals =
        #[[0,10],[14,14],[15,20]]
        #newInterval =
        #[11,11]

        #Output: [[0,10],[11,11],[14,14]]
        #Expected: [[0,10],[11,11],[14,14],[15,20]]

        #Turns out it was just the fault of the middle no overlap case jumping
        #i+=2 which can skip an interval[i], instead just while loop and append 
        #the rest right after case is determined 


        #BIG TAKEAWAY FOR INTERVAL MERGES 
        #1. No overlap (left, middle of two existing, right)
        #2. Complete overlap (new completely overlaps existing, existing completely
        #overlaps new)
        #3. Partial overlap (new causes a left leaning/seeking merge overlap, new
        #causes a right leaning/seeking merge overlap)
      

        #for partial case, need to init start and end with min and max, just do 
        #that 
        #Got the two example cases, imma hunt for more cases now  

        #1. New intervals before all intervals X
        #2. New interval after all intervals X
        #3. New interval between two non overlapping intervals X
        #4. New Interval Completely Overlapping an Existing Interval X
        #5. New Interval Completely Overlapped by an Existing Interval X
        #6. New Interval Partially Overlapping with One Interval X
        #7. New Interval Partially Overlapping with Multiple Intervals X
        #8. New Interval covering multiple intervals X
        #9. Empty list of intervals X
        #10. Exact overlap with an existing interval X
        #11. Touching intervals: X

        #intervals = [[1, 2], [5, 6]], newInterval = [2, 5]
        #Output: [[1,5], [5,6]]     should be [1,6]

        #This problem is deadass demonic bruh, testing all 11 cases in VS code
        #and they all good and theres still more shit to consider damn 

        #intervals =
        #[[0,10],[14,14],[15,20]]
        #newInterval =
        #[11,11]

        #Output: [[0,10],[11,11],[14,14]]
        #Expected: [[0,10],[11,11],[14,14],[15,20]]

        #Turns out it was just the fault of the middle no overlap case jumping
        #i+=2 which can skip an interval[i], instead just while loop and append 
        #the rest right after case is determined 

        #Reached the goal post! 

        #BIG TAKEAWAY FOR INTERVAL MERGES 
        #1. No overlap (left, middle of two existing, right)
        #2. Complete overlap (new completely overlaps existing, existing completely
        #overlaps new)
        #3. Partial overlap (new causes a left leaning/seeking merge overlap, new
        #causes a right leaning/seeking merge overlap)


        #Someone pointed out in the discussions that you can simply insert 
        #the new interval into the intervals array (just find where to place such
        #that the starts are still ordered) and then just use the exact code 
        #from Merge Intervals to do the merging. Honeslty mad mad smart: 

        array=[]
        n=len(intervals)
        i=0 
        while i<n and intervals[i][0]<newInterval[0]: 
            array.append(intervals[i])
            i+=1 
        array.append(newInterval)
        while i<n: 
            array.append(intervals[i])
            i+=1 
        
        result=[]
        i=0 
        n=len(array)
        while i<n: 
            current_start, current_end=array[i]
            j=i+1 
            while j<n and current_end>=array[j][0]:
                current_end=max(current_end, array[j][1])
                j+=1 
            result.append([current_start, current_end])
            i=j 
        return result 
        
       