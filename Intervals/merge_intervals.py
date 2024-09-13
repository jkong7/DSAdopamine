class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        result=[]
        i=0 
        n=len(intervals)
        while i<n: 
            j=i+1 
            current_start, current_end=intervals[i]
            while j<n and current_end>=intervals[j][0]: 
                current_end=max(current_end, intervals[j][1])
                j+=1 
            i=j
            result.append([current_start, current_end]) #Either merged or not merged
            #current_end will store the correct case every time 
        return result
        #Coded again for clarity, think of it as a chase between the max end 
        #and the next start, if the current_end can match next_start, it 
        #expands/merges



        #Sort the intervals based on the start will make it easy 
        #Keep track of starts, and if the end of one interval is greater than or 
        #equal to another start, merge those into start 1, end 2

        intervals.sort() #nlog n
        result=[]
        n=len(intervals)
        i=0 
        j=1
        result=[]
        while i<n: #O(n) two pointer scan 
            current_start, current_end=intervals[i][0], intervals[i][1]
            max_end=current_end
            while j<n: 
                if max_end>=intervals[j][0]: 
                    max_end=max(max_end, intervals[j][1])
                    j+=1 
                else: 
                    break 
            i=j 
            result.append([current_start, max_end])
        return result 

        #Honestly, what helps the most is the visualization and the intervals 
        #are easy to draw and visualize. 
        #The ultimate solving insight was that we need to keep track of the max_end
        #and update that IF the max end is larger than the next start. If its not
        #larger than the next start, we break out the loop. i will always be the 
        #new start and j will find new intervals to the right to merge 

        #---------- max_end>=intervals[j][0], update max_end
        # ---------------- max_end>=intervals[j][0], update max_end
        #   -------------------    <--max_end

        #------------------- max_end<intervals[j][0], break out loop, i=j=1
        #                         ---------- <----next start (i)

        #Here's it a little cleaned up. Also note that j=i+1 avoid a redundant 
        #first while loop iteration check. By just setting i=j, the first check
        #is comparing the interval with itself. j should be set to i+1 each iteration
        #(j is the fetcher pointer, i stays home)
        #i is the index that identifies the start of the current interval being 
        #considered for merging 
        #j moves ahead to find intervals that overlap with the i interval 


        intervals.sort()
        result=[]
        n=len(intervals)
        i=0 
        result=[]
        while i<n: 
            j=i+1
            current_start, current_end=intervals[i][0], intervals[i][1]
            while j<n and current_end>=intervals[j][0]: 
                current_end=max(current_end, intervals[j][1])
                j+=1 
            i=j #Move to the next non-overlapping interval 
            result.append([current_start, current_end])
        return result




        #Also coded up the standard for loop approach: 

        intervals.sort()
        n=len(intervals)
        result=[intervals[0]]
        for i in range(1, n): #Start it one to the right of first element
            last_start, last_end=result[-1][0], result[-1][1]
            new_start, new_end=intervals[i][0], intervals[i][1]

            if last_end>=new_start: 
                result[-1]=[last_start, max(last_end, new_end)]
            else: 
                result.append(intervals[i])
        return result
        
 #Note about greedy merge (technique used both in "merge intervals" and "insert intervals"): 
 #In computational algorithms involves merging overlapping or adjacent intervals 
 #by always taking the next interval that can be combined with the current one,
 #without considering future intervals, hence the term "greedy" because it
 #makes a locally optimal choice at each step. Merging intervals is considered
 # a greedy merge because it involves sorting intervals by their starting points 
 #and then iteratively merging them based on immediate conditions (overlap or adjacency). 
 #This approach prioritizes immediate optimization and reduction of the list size without 
 #backtracking, typical of greedy algorithms used to efficiently reduce a set of potentially 
 #overlapping intervals to a minimal set of non-overlapping intervals.