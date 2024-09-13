class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        #kth largest is size k heap and popping when size above k and using minheap

        intnums=[int(num) for num in nums]
        import heapq
        heap=[]

        for num in intnums: 
            heapq.heappush(heap, num)
            if len(heap)>k:
                heapq.heappop(heap)
        return str(heap[0])