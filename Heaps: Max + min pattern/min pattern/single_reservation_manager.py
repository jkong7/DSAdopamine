class SeatManager(object):
    import heapq

    def __init__(self, n):
        """
        :type n: int
        """
        self.heap=[]
        self.counter=1 
        heapq.heappush(self.heap, self.counter)

        

    def reserve(self):
        """
        :rtype: int
        """
        self.counter+=1 
        r=heapq.heappop(self.heap)
        heapq.heappush(self.heap, self.counter)
        return r
        

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        heapq.heappush(self.heap, seatNumber)

    #There we go, initially did brute heap way of adding all n numbers to heap 
    #But I optimized by just starting with the first number (1) then when you call
    #reserve just pop and then add the next self.counter (+=1). Unreserve is still
    #the same pushing to the heap 
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)