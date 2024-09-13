class Solution(object):
    def maxArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #This should just be greedy and merge traversing from right to left. Becuase 
        #why would you want to do it left to right that just carries the risk of 
        #the left number being larger than the right and then we can't do another 
        #merge. Going from the right always makes sure the right is larger which is 
        #what we want to be able to do as many merges as possible 

        for i in range(len(nums)-2, -1,-1): 
            if nums[i]<=nums[i+1]: 
                nums[i]=nums[i]+nums[i+1]
        return nums[0]