class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #When you can take any order and you want to min/max, you should sort, its 10^5 
        #so yeah you should sort 

        #To minimize, take left right pairs and then move left+=1 and right-=1. Because
        #think if you dont pair rightmost with a left for say, then that rightmost 
        #will eventually HAVE to be paired with a num larger than leftmost and that 
        #makes that pair greater than if you just paired leftmost and rightmost. So 
        #yeah thats always the most optimal, so return max sum of such pairs 

        nums.sort()
        left,right=0, len(nums)-1
        maxx=0 
        while left<right: 
            maxx=max(maxx, nums[left]+nums[right])
            left+=1 
            right-=1 
        return maxx
