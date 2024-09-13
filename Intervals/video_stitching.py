class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        #Sort clips by start value is no brainer 
        #AND also sort secondary by end times since my greedy algo is simply just gonna
        #look at the largest end values 

        clips.sort(key=lambda x:(x[0], x[1]))

        #Note that the first clip must start with a 0
        #I think for each start value, we are simply looking for the largest end value
        #the start value then can be in the range [start, currentend]. Then if current
        #end 

        maxend=-1 
        for i, clip in enumerate(clips): 
            if clip[0]!=0: 
                break 
            else: 
                maxend,index=max(maxend, clip[1]), i
        if maxend==-1: 
            return -1 
        if maxend>=time: 
            return 1 


        i=index 
        count=1 
        n=len(clips)
        while i<n: 
            j=i+1 
            end=maxend
            while j<n and clips[j][0]<=end: 
                maxend=max(maxend, clips[j][1])
                j+=1 
            if end==maxend: 
                return -1 
            count+=1 
            i=j-1 
            if maxend>=time: 
                return count 
        return count if maxend>=time else -1 
        #Got like 90% of it, just couldn't figure out for the life of me why tf it wasn't
        #working with that test case. Only two minor corrections, first add a checker 
        #that if end==maxend, return -1 early bc that means no progress was made and 
        #we just can't reach time 

        #And its i=j-1 not i=j, AHH because maxend is one behind j, we need i to be the
        #last used clip in the iteration or else i=j skips the jth clip on the next 
        #iteration (i=j and j=i+1 will skip it )

        #Aight and then I needed to also cover the case the first 0 chain already 
        #covered time and then return 1 
