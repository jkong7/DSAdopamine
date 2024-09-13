class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #I think the goal is to just get the largest partition from the array and '
        #just return its sum, a partition is valid if the sum of all its nums except
        #the largest num is greater than the greatest num. So im thinking first sort 
        #Yup 10^5 constraint

        #Im also thinking prefix sums to check if a partition is valid?

        #I think that more numbers always helps so we can always start and consider 
        #from the front

        #yeah so then starting from the front, its greedy, go as far as you can before
        #invariant breaks, and we simply check invariant using a rolling prefix sum 
        #Prefix sum also conveniently tracks the perimeter for us so we can just return
        #that 

        nums.sort()
        prefix=nums[0]+nums[1]
        found=False
        for i in range(2, len(nums)): 
            if prefix>nums[i]: 
                per=prefix+nums[i]
                found=True
            prefix+=nums[i]
        return per if found else -1

        #Yup, nice breakthrough, we basically just need to track the farthest 
        #point in the sorted array that prefix>nums[i] (ie sum of all sides except
        #largest is greater than largest). That conditional will make sure per is on
        #the last seen/farthest right instance of this which is the largest per. If this
        #conditional is reached even once, there is a valid polygon so we mark a flag
        #as true. Return per if flag true else -1
        #Cool problem, really fun 
        #checked the tags after and I basically did exactly that lmao, greedy, sorting,  
        #prefix sum 
        #O(n) time O(1) space 