class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        count=0 
        n=len(nums)
        heap=[]
        for num in nums: 
            heapq.heappush(heap, num)
        while True:
            first = heapq.heappop(heap)
            if first >= k: 
                return count 
            second = heapq.heappop(heap) 
            insert = (min(first, second) * 2) + max(first, second) 
            heapq.heappush(heap, insert) 
            count+=1
        #Heap: Use heap to extract lowest two values, if the first extracted value is already >=k, we have 
        #satisfied the condition so return count. Otherwise, another iteration is needed, so get the value
        #from the two heap pops and then push back, continue, heap will always shrink so this return will 
        #always be hit 

