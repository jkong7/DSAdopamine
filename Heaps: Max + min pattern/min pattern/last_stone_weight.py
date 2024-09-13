import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        #Heaviest two stones 
        #We want a heap of size 2 probably that continuously tracks this 
        #stones array changes dynamically  XX

        #heapify converts an array to a minheap in O(n)
        #can first invert all elements in array and then heapify to have a maxheap

        if len(stones)==1: 
            return stones[0]

        maxheap=[-x for x in stones] #maxheap, first just make negative all values 
        heapq.heapify(maxheap) #O(n)

        #Pop twice, push (or don't push if x==y)
        while len(maxheap)>1: #nlogn
            x=heapq.heappop(maxheap) 
            y=heapq.heappop(maxheap)
            if x==y: 
                continue 
            else: 
                heapq.heappush(maxheap, -abs(x-y)) #reverse, maintain negative values 

        return 0 if len(maxheap)==0 else -maxheap[0]
