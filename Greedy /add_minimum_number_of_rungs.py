class Solution(object):
    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        #This is just greedy, we HAVE to be able to fill in the gaps whenever 
        #we meet one 
        import math 
        rungs=[0]+rungs 
        add=0 
        for i in range(len(rungs)-1): 
            if rungs[i]+dist<rungs[i+1]: 
                add+=int(math.ceil((rungs[i+1]-rungs[i]-dist)/float(dist))) 
        return add
        # the number of adds you have to do is just an O(1)

        