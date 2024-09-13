class SummaryRanges(object):

    def __init__(self):
        self.intervals=[]
        

    def addNum(self, value):
        """
        :type value: int
        :rtype: None
        """
        #Maintain sorted order for bin search using insert, and then use bin search
        #to find where to insert. Then three cases: grow the left, grow the right, 
        #or create a new [val, val] interval
        #And one extra case to consider: value brings together the left-1 and left
        #intervals into one 
        #And the case where the value is already in an interval, do nothing then 
        def condition(targetnumber): 
            return targetnumber>=value
        left,right=0, len(self.intervals)
        while left<right: 
            mid=left+(right-left)//2
            if self.intervals[mid][0] <= value <= self.intervals[mid][1]:
                return  # Value is already covered by an existing interval, return
                #with no changes
            if condition(self.intervals[mid][0]): 
                right=mid
            else: 
                left=mid+1
        #Left is now insertion index and left-1 is left interval and left
        #is right interval 
        #Bin search guarantees that we are only operating/need to look at 
        #left-1 and left intervals 
        leftmerge=left>0 and value==self.intervals[left-1][1]+1
        rightmerge=left<len(self.intervals) and value==self.intervals[left][0]-1
        if leftmerge and rightmerge: #Value merges the two together
            self.intervals[left-1][1]=self.intervals[left][1]
            self.intervals.pop(left) #Remove right interval and change left interval
        elif leftmerge: #Expand the left
            self.intervals[left-1][1]=value
        elif rightmerge: #Expand the right 
            self.intervals[left][0]=value
        else: #Insert new [value, value] interval
            self.intervals.insert(left, [value, value])
        
    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        return self.intervals


    #Time complexity: Bin search is logn, in the 3/5 cases of value already in 
    #interval, only left expand, only right expand, the expansions/do nothing 
    #are O(1) so logn total. However, in the other two cases, there is pop and 
    #insert which are O(n) (these methods are O(n) because of the need to shift
    #elements)

    #Binary search insertion is super powerful! Three interval questions using 
    #search insert position pattern! 
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()