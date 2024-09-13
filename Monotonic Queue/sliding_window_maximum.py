from collections import deque 
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        #follow up with the if l>q[0] q.popleft() check to keep the bounds of the q
        #up to date with the newest window. Here, we don't really have a "valid" 
        #window check, it just must be of length k which we keep steady once we
        #reach that and l and r are incremented together. Here we just need access
        #to the max element of every window which maxq[0] provides!


        maxq=deque() #Mono dec
        result=[]
        l=0 
        for r in range(len(nums)): 
            while maxq and nums[r]>nums[maxq[-1]]: 
                maxq.pop()
            maxq.append(r)
            if r-l+1==k: 
                result.append(nums[maxq[0]])
                l+=1 
                if l>maxq[0]: 
                    maxq.popleft()
        return result 



        #MONOTONIC QUEUE, decreasing order queue 
        #The reason we want to use a queue is because we want constant time to 
        #add/remove from both the right and left 

        #IMPORANT: Mono decreasing queue, the max element will always be on the LEFT
        #of the queue 
        #Ex queue: [8 6 5 3 2 1]
        #           l         r
        #           max

#Yes, you typically use both queue[0] to access the maximum (left element) and queue[-1] to maintain the monotonic order (right element). 

#So if number is GREATER than the right element, you pop right from the queue (same
#exact idea as mono stack)

#And if the length of the window exceeds k, you pop from the left of the queue

#The max element in the window is always accessed by the left, sw[0]

        result=[]
        q=deque() #q holds INDICES
        l=0 
        for r in range(len(nums)): 
            while q and nums[r]>nums[q[-1]]: #See same as mono stack, while mono
            #decreasing invariant is not true, pop (pop from the right)
                q.pop()
            q.append(r) 
            #^^^This all looks the exact same as using mono dec stack 

            #If leftmost of the queue is no longer in bounds of the window, popleft:
            #(Can't be considered anymore)
            if l>q[0]: 
                q.popleft()
            if (r-l+1)==k: #Valid windows are length k, r-l+1 is length of window
                result.append(nums[q[0]])
                l+=1 
        return result 

        #Note this is still a fixed size sliding window of size k, once the width
        #of window gets to k, l and r will always be incremented together 
        #left will always then move one ahead of q[0] index so q[0] needs to be 
        #removed via popleft, then the mono comparison with nums[r] and top/right 
        #of queue to make sure the left is always the max element 
