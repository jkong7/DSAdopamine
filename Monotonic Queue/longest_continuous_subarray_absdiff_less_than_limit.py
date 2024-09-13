from collections import deque 
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        #For each subarray, we need constant time access to both the min and max 
        #elements
        #So keep two queues? One mono dec for max [8 5 4 3]
        #                    One mono inc for min [1 2 3 4]

        #Finding the longest length so max r-l+1 variable 

        result=0 
        l=0 
        minq=deque() #Will store indices, should be this way always
        maxq=deque() #Will store indices, should be this way always 
        for r in range(len(nums)): 
            while maxq and nums[r]>nums[maxq[-1]]: 
                maxq.pop()
            maxq.append(r) #Maintain maxq mono dec order (right compare)

            while minq and nums[r]<nums[minq[-1]]: 
                minq.pop()
            minq.append(r) #Maintain minq mono inc order (right compare)

            #While loop for when the window condition is NOT true 
            while nums[maxq[0]]-nums[minq[0]]>limit: #[0]/left is max/min 
                l+=1 

                #This is present in every one of these questions: popleft from q
                #if new left bound exceeds the leftmost q bound
                if l>maxq[0]: 
                    maxq.popleft()
                if l>minq[0]: 
                    minq.popleft()
            #Window is valid!
            result=max(result, r-l+1)
        return result 
