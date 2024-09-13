"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #Equivalent prompt: What is the maximum number of overlapping 
        #intervals at any given time? 
        #Yeah I think this is super super similar to min number of 
        #arrows to burst balloons 
        #That one was one arrow to burst all arrows in the immediate 
        #shrinking interval 
        #Can probably use same greedy approach here 

        #Nevermind^^ That discards a current overlapped interval 
        #once it no longer linearly overlaps but they can overlap 
        #with future intervals, can't do that

        #Clever sorted two array start and end times neetcode solution:
        #As long as start<end, increment count and increment start 
        #pointer, means we are able to start another interval in the merge
        #Once this is no longer true, it means an interval has started
        #outside the range so add on another end (increment) and then 
        #at that point, one less interval is in the range so decrement count

        start=[]
        end=[]
        for interval in intervals: 
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        s,e=0,0
        result, count=0,0
        while s<len(start): 
            if start[s]<end[e]:
                s+=1 
                count+=1 
            else: 
                e+=1 
                count-=1 
            result=max(result, count)
        return result 

        #Using a minheap: Pop if current start is after the min 
        #element (least end time) as it means there is no more overlap
        #Always push the current end time onto the heap 
        #The heap will always track the least end time which is how 
        #we determine whether to pop or not (also same +=1 -=1 logic)
        #The length of the heap at the end is the max number of 
        #overlapping intervals 

        if not intervals:
            return 0 
        intervals.sort(key=lambda x: x.start)
        heap=[]
        heapq.heappush(heap, intervals[0].end)
        for i in range(1, len(intervals)): 
            if intervals[i].start>=heap[0]: 
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
        return len(heap)
        #Greedy minheap (least end) vs current start approach 
