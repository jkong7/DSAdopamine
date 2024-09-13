import heapq 
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k=k 
        self.nums=nums 
        self.heap=[]

        for num in self.nums: 
            heapq.heappush(self.heap, num)
            if len(self.heap)>self.k: 
                heapq.heappop(self.heap) #nlogk
        
    def add(self, val): #logk
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap)<self.k: 
            heapq.heappush(self.heap, val)
        elif val<=self.heap[0]: 
            return self.heap[0]
        else: 
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
        #Got it, maintain a size-k heap (do this in the initialization) such that 
        #heap[0] is the kth largest element 
        #Then, when adding, if val<=heap[0], the kth largest is still heap[0] so 
        #simpy return that 
        #if val>heap[0], do a pushpop with val and then return heap[0] as push pop
        #maintain the invariability 
        #There's also the case where len(nums)<k so the heap has len less than k, 
        #in that case, push the new element and stil return heap[0], might be 
        #technically the 6th largest, same as 7th, 8th, etc largest in this context
        #'Stream': nums keeps growing as new values are added 
        


### Summary:
#- **Nums grows**: Continuously adds new elements.
#- **Heap size**: Stays at \( k \).
#- **Heap[0]**: Always the \( k \)-th largest element.

#Note: In the __init__ method, self.k is used because k is needed throughout 
#the class to maintain the size of the heap. self.nums is not needed because 
#the initial list of numbers is used only during initialization to build the heap.


    
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)