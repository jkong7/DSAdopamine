class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #This is sliding window??
        #Yeah if num of distinct elements exceeds, then you shrink from the left
        #I'll use a set to maintain dynamic unique-elements count of the window 

        #Yeah this is a count SW where you need to move l to tipping point and then 
        #increment with l+1, okay the tipping point is where there is more than 1 
        #of an element and the uniquecount is already equal, okay yeah so use a dict
        #instead of set for the window so you can track freq too 

        from collections import Counter 
        from collections import defaultdict 
        count=Counter(nums)
        unique=len(count) 

        result=0 
        l=0 
        uniquecount=defaultdict(int)
        for r in range(len(nums)): 
            uniquecount[nums[r]]+=1 
            while len(uniquecount)>unique or (l<r and uniquecount[nums[l]]>1): 
                uniquecount[nums[l]]-=1 
                l+=1 
            if len(uniquecount)==unique: 
                result+=l+1 
        return result 
