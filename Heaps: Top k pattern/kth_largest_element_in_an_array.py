class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #1. Start with empty heap, keep pushing and pop when length heap exceeds k
        #will always cutoff the smallest element with the k+1 size leaving the end
        #as the k largest/frequent elements
        import heapq
        heap=[]
        for i in range(len(nums)): 
            heapq.heappush(heap, nums[i])
            if len(heap)>k: 
                heapq.heappop(heap)
        return heap[0]
        #Can also do what I did in top k freq elements, keep pushing until size 
        #exceeds k, then pop, the end will be the k largest elements and heap[0]
        #will be the minimum of the top k largest elements which is the kth largest

        #-------------------------------------------------------------
        
        #2. Start with heap with first k elements, pushpop remaining nums elements
        #that have a value larger than min element in heap heap[0][0]
        
        #If you maintain a heap with k elements and keep puush popping, 
        #Then at the end of the loop through nums, there will be k elements
        #and the MINIMUM of the heap (O(1) lookup) will be the smallest of the 
        #k largest elements which is the kth largest element
        #A new candidate nums[i] must be larger than the min of the current heap 
        #heap[0] in order to replace it (then at the end, it will be k largest
        #elements)
        #For example, if its [5,4,4,3] and you still must consider [2,1], you would
        #not pushpop with 2 bc then 3 would be replaced by 2 and its no longer 
        #k largest elements 
        heap=nums[:k] #First k elements, keep heap at k elements 
        heapq.heapify(heap)
        for i in range(k, len(nums)): 
            if nums[i]>heap[0]: 
                heapq.heappushpop(heap, nums[i])
        return heap[0]
        #nlogk
        
        #-------------------------------------------------------------
        
        #3. Inefficient nlogn
        heapq.heapify(nums)
        for _ in range(len(nums)-k): 
            heapq.heappop(nums)
        return nums[0]
        #nlogn


        #SUPER IMPORTANT: Most kth largest/smallest heap problems will have its most
        #efficient solution by keeping the heap at max size k-nlogk instead of nlogn