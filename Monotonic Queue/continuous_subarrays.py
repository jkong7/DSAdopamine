from collections import deque 
class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #So subararys such that the max absolute difference is 2 
        #We need minq for min element in the window and maxq for max element in the 
        #window 

        count=0 
        minq=deque()
        maxq=deque()
        l=0 
        for r in range(len(nums)): 
            #Identical to mono stack invariant popping and then appending after:
            #Like other SW problems, r always gets processed/added/counted somehow
            #Here its being inserted/invariant restore by the mono qs
            #RIGHT/TOP of q is [-1]
            while maxq and nums[r]>nums[maxq[-1]]: 
                maxq.pop()
            maxq.append(r)
            
            while minq and nums[r]<nums[minq[-1]]: 
                minq.pop()
            minq.append(r)
        
            #Use the min/max from the queues to pose invalid window condition: 
            #We fix by shrinking from the left and then q popping from left 
            #if the boundary is no longer valid for the current l window 
            #LEFT/MAX/MIN of q is [0]
            while nums[maxq[0]]-nums[minq[0]]>2: 
                l+=1 

                if l>maxq[0]: 
                    maxq.popleft()
                if l>minq[0]: 
                    minq.popleft()

            #Now, every subarray between l and r are valid: increment using r-l+1: 
            count+=r-l+1
        return count 


        #REMEMBER SUPER IMPORTANT WITH SW COUNT: Here we use count+=r-l+1 to represen
        #that EVERY SUBARRAY BETWEEN an l and r are valid. r-l+1 counts all subarrays
        #formed with each new extention of r. So you are counting every possible 
        #subarray that meets the condition for every position of r in the array

        #Note l+1 is used to say that every subarray from the start and ending at l
        #is valid

#Yes, that's mostly correct:

#- **`l+1`** isn't specifically used here, but if mentioned, it typically represents the count of all elements up to and including index `l`. It could be used in contexts where every subarray ending at index `l` is considered.
  
#- **`r-l+1`** indeed represents the number of all possible subarrays starting from any position between `l` and `r` (inclusive) and ending at `r`. This calculation ensures that you're counting every valid subarray within the window defined by `l` and `r`.

#Why if window from l to r is valid, every window within that range is also valid: 

#This is because any smaller subarray within l to r inherits the same range and thus the same minimum and maximum values, ensuring the condition is met throughout.
#Therefore, if the entire window from l to r is valid, every subarray within this window is also valid.