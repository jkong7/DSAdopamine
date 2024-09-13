class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Find the subarray containing unique elements that has the max sum, since its 
        #all positive numbers, sliding window, max length->max sum should work 
        from collections import defaultdict
        l=0 
        summ=0
        maxx=0 
        ht=defaultdict(int)
        for r in range(len(nums)): 
            ht[nums[r]]+=1 
            summ+=nums[r]
            while ht[nums[r]]>1: 
                ht[nums[l]]-=1 
                summ-=nums[l]
                l+=1 
            maxx=max(maxx, summ)
        return maxx 