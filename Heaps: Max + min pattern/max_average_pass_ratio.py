class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        import heapq 
        heap=[]
        n=len(classes)
        average=0 
        for c in classes: 
            add = (float(c[0]+1) / float(c[1] + 1)) - (float(c[0])/float(c[1]))
            average+=float(float(c[0])/float(c[1]))/float(n)
            heapq.heappush(heap, (-add, c))
        while extraStudents>0: 
            add, classes = heapq.heappop(heap)
            average+=float((-add))/float(n) 
            newclasses = [classes[0]+1, classes[1]+1]
            newadd = (float(newclasses[0]+1)/float(newclasses[1]+1)) - (float(newclasses[0])/float(newclasses[1]))
            heapq.heappush(heap, (-newadd, newclasses))
            extraStudents-=1 
        return average 

        #Maintain maxheap with the differences (adding a student versus not) and 
        #it should also include the [pass, total] array. Each time pop the largest
        #difference to add to the average and then push in the new difference and new
        #array which is now [pass+1, total+1]
