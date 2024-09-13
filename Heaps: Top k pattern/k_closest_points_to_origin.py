import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        #k closest points 
        #Just immediately jump to an nlogk solution 
        #Maintain a size k heap 
        #Here, maintain a size k maxheap, so pops will be made to the 
        #largest negative number (which is the functional min in the heap)
        #Thus heap will keep the k distances with the smallest absolute values 
        #Afterwards just extract the coords associated with the k smallest 
        #distances in the heap 
        
        #8 9 10 11 12    k=3
        #return 8 9 10  [-10, -9, -8]. heap[0]=-10 
        heap=[]
        for coords in points: #O(n logk)
            distance=coords[0]**2 + coords[1]**2 
            heapq.heappush(heap, (-distance, coords))
            if len(heap)>k: 
                heapq.heappop(heap) #pops the largest abs value distance (smallest actual number since negative values)
        #Now you have a size k heap with the k smallest distances, extract coords:
        result=[]
        for dist, coords in heap: #O(k)
            result.append(coords)
        return result 
        #O(n logk)
#Note: Yes, to find the k furthest points, you would use the exact same code but
#use distance instead of -distance:

        