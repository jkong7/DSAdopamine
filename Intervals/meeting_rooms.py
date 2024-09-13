"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        n=len(intervals)
        i=0 
        while i+1<n: 
            if intervals[i].end>=intervals[i+1].start:
                return False 
            i+=1 
        return True 
        
        #Equivlalent to "Given a list of intervals, determine if there
        #is any overlap"
        #Overlap exists if the start of i+1 interval comes before or at 
        #the end of the i interval 
        #intervals[i].end>=interavls[i+1].start:
        #------------
        #        ----------