class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        #Just make precomputation stash of max value STARTING at value so then 
        #for each interval, you simply add its value to max value at 1+end 

        #For the precomputation, I think we can use a hashtable so O(n) space 
        #and then O(n) loop where each interval computation is O(1) lookup 

        #Sort events, compute suffix maximum by just going backwards through the 
        #events array. Then do an O(n) loop through and for each end of an event
        #find the first index that doesn't overlap (end+1) using binary search 
        #precomputed suffix gives the max for that portion 

        events.sort()
        suffix=0
        for i in range(len(events)-1, -1, -1): 
            suffix=max(suffix, events[i][2])
            events[i].append(suffix)

        def BS(targetnumber): 
            def condition(index): 
                return events[index][0]>=targetnumber 
            left,right=0, len(events)-1 
            while left<right: 
                mid=left+(right-left)//2
                if condition(mid): 
                    right=mid
                else: 
                    left=mid+1 
            return left if events[left][0]>=targetnumber else -1 

        maxx=0 
    
        for i in range(len(events)): 
            secondhalfindex=BS(events[i][1]+1)
            if secondhalfindex!=-1: 
                cur=events[i][2]+events[secondhalfindex][3]
            else: 
                cur=events[i][2]
            maxx=max(maxx,cur)
        return maxx 

        #At the end had to deal with case where its just one interval 
        #(there is no interval to its right that could be its pair), so in BS just 
        #check if events at index left is ACTUALLY larger than targetnumber, if not 
        #we know it doesn't have a matching pair 
