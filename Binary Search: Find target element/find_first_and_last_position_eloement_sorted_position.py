class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Last position is just left-1 when doing targetnumber>target because it will 
        #give you the leftmost of the first occurence of a number larger than target
        #To its left 1 is the target 

        #First position is just left when doing targetnumber>=, leftmost occurence
        #of number >=target 


        if not nums: 
            return [-1,-1]

        def last_s(mid): 
            return nums[mid]>target
        def first_s(mid): 
            return nums[mid]>=target 


        last,right=0, len(nums)-1 
        while last<right: 
            mid=last+(right-last)//2
            if last_s(mid): 
                right=mid
            else: 
                last=mid+1 

        first, right=0, len(nums)-1 
        while first<right: 
            mid=first+(right-first)//2
            if first_s(mid): 
                right=mid
            else: 
                first=mid+1 

        if nums[-1]==target: 
            return [first,len(nums)-1]
        return [first, last-1] if nums[first]==target and nums[last-1]==target else [-1,-1]

        #Last position: Find leftmost element that is greater than target, then ret
        #left-1 which will be last position of target 
        #First position: Find leftmost element that is greater than or equal to 
        #target, that is the first position 

        #Edge case: Last position is last elem of array, then we can't use BS to 
        #determine leftmost GREATER than target, so we manually check if last elem
        #is target and then use same first paired with last element 

        #And then also return [-1,-1] if not one of the conditions 
