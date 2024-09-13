class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #Simulating maxheap by sorting using -value. This is nlogn since the 
        #size of the heap can grow to n
        import heapq
        numdict={}
        for num in nums: 
            if num in numdict: 
                numdict[num]+=1 
            else: 
                numdict[num]=1 #O(n)
        heap=[]
        for key,value in numdict.items(): 
            heapq.heappush(heap, (-value, key)) #nlogn
        result=[]
        for _ in range(k): 
            value, key=heapq.heappop(heap) #klogn
            result.append(key)
        return result
        
        #-------------------------------------------------------------
        #nlogk solution: limiting the heap to grow only to k. Iterating through the 
        #entire HT and using a minheap but then popping when len>k will remove 
        #the smallest elements and at the end of the loop, leave only the k 
        #largest elements in the heap 
        import heapq
        numdict={}
        for num in nums: 
            if num in numdict: 
                numdict[num]+=1 
            else: 
                numdict[num]=1  #O(n)

        #-------------------------------------------------------------
        #1.Start with heap with first k elements, pushpop remaining nums elements
        #that have a value larger than min element in heap heap[0][0]
        numdict_items=list(numdict.items())
        heap=[(freq,num) for num,freq in numdict_items[:k]]
        heapq.heapify(heap)
        for key, value in numdict_items[k:]: 
            if value>heap[0][0]: #first heap element (min), access its freq
                heapq.heappushpop(heap, (value, key)) #nlogk

        #2.Start with empty heap, keep pushing and pop when length heap exceeds k
        #will always cutoff the smallest element with the k+1 size leaving the end
        #as the k largest/frequent elements
        heap=[]
        for key,value in numdict.items(): 
            heapq.heappush(heap, (value, key)) #nlogk 
            if len(heap)>k: 
                heapq.heappop(heap)

        #-------------------------------------------------------------
        result=[]
        for _ in range(k): 
            value, key=heapq.heappop(heap) #klogk
            result.append(key)
        return result
        
        
        
        #Binary heap theory review: insert, delete, and extract_min are all O(log n)
        #since all require reorganization (either bubble up or percolate down). 
        #This is efficient 
        #A binary heap is especially useful in scenarios where you need to
        #efficiently find the "most something" or the "top k something" due to 
        #its properties of sorting and efficient extraction 
