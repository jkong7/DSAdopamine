class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """

        indexdict={}
        for i in range(len(intervals)): 
            indexdict[intervals[i][0]]=i  

        #Each interval start is unique 

        #Begin by sorting
        unsorted=list(intervals)
        intervals.sort() #O(n logn)


        #Binary search!!

        #The solution is probably n logn (one binary search logn for every interval)

        def bin_search(start): 

            def condition(targetnumber): 
                return targetnumber>=start
            left, right=0, len(intervals)
            while left<right: 
                mid=left+(right-left)//2
                if condition(intervals[mid][0]): 
                    right=mid 
                else: 
                    left=mid+1 
            return left if left!=len(intervals) else -1 
        result=[]
        #Input start to binary search will be the end of the interval 
        for interval in unsorted: 
            index=bin_search(interval[1])
            if index==-1: 
                result.append(-1)
            else: 
                result.append(indexdict[intervals[index][0]])
        return result
        #I used an unsorted original list to 
        #iterate through at the end which found the ORIGINAL indexes of the 
        #bin search return insertion index and that combo correctly maps 
        #the original intervals in order to the original insert indexes 

        #Binary search is used on each END of the intervals to determine 
        #the FIRST start position that is >= that end and the interval with 
        #that start is the right interval (so we want that index from the 
        #indexdict which mapped starts to indexes and note the problem tell us
        #that all starts are unique)

        #And of course bin search is applied on the SORTED starts of the intervals
        #so it just becomes find insert position. Ex: [1,3,7,10,12,13] find right
        #start for end=11 will be 12. 

        #Oh also if left==len(intervals), that means there isn't a start value
        #that is >= that end so there is no right interval so that is the -1 case

        #Coded it up again for clarity:

        indexdict={intervals[i][0]: i for i in range(len(intervals))}
        unsorted=list(intervals)
        intervals.sort()
        def bin_search(end): 
            def condition(targetstart): 
                return targetstart>=end
            left, right=0, len(intervals)
            while left<right: 
                mid=left+(right-left)//2
                if condition(intervals[mid][0]): 
                    right=mid
                else: 
                    left=mid+1 
            return left if left!=len(intervals) else -1 
        result=[]
        for start, end in unsorted: 
            index=bin_search(end)
            result.append(-1 if index==-1 else indexdict[intervals[index][0]])
        return result




        