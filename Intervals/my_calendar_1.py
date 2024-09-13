class MyCalendar(object):

    def __init__(self):
        self.intervals=[]
        
    def book(self, start, end): #O(n)
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        #I'm going to try binary search + sorting: 
        #FFFTTT, return FIRST number with the condition >=start, this is the 
        #insertion index 
        #Note, we will have the index to perform insertion but insertion will 
        #still always be O(n) in the worst case

        #This part is equivalent to search insert position (useful skill/pattern): 
        def condition(targetnumber): 
            return targetnumber>=start 

        left,right=0, len(self.intervals) #Search space is the indices of start array 
        while left<right: 
            mid=left+(right-left)//2
            if condition(self.intervals[mid][0]): 
                right=mid #Could be right or could be to the left of right 
            else: 
                left=mid+1 

        #Now, left is the insertion index, only need to compare against the 
        #previous and one after intervals of the proposed insertion index 

        #. left-1                left
        #--------------          -----------
        #                  ---
        #.  --- XX <               > ---X 

        if (left>0 and start<self.intervals[left-1][1]) or (left<len(self.intervals) and end>self.intervals[left][0]): 
            return False

        #If no overlap, insert at the binary search found index left and return True
        self.intervals.insert(left, [start, end])
        return True 

        #170-190 ms, good runtime copared to for loops which was like 1000ms



        #This is the brute force O(n) approach (needs to scan intervals array with
        #each call), grows more inefficient as more intervals are added: 

        #Intervals will always be guaranteed to have non overlapping intervals b/c:
        #Return true AND put interval if it doesn't overlap with existing intervals
        #Return false AND do not put interval if it does overlap 
        for interval in self.intervals: 
            if interval[0]<=start<interval[1] or interval[0]<end<=interval[1] or (start<interval[0] and end>interval[1]): 
                return False 
        self.intervals.append([start, end])
        return True 

        

        
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)