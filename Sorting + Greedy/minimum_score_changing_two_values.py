class Solution(object):
    def minimizeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #I think: Sort, iterate, the low score is the min of the adj differences 
        #The high score is the diff between last and first elem
        #With one element change to nums, you can always make the low score 0 

        #Okay okay, you can just make the first two elements of the sorted array 
        #equal to the third and that would minimize the max, if you dont do the first 
        #2, the max will come from one of those which is always larger. The answer then 
        #is just last elem minus third elem, if length 3 then its 0 

        #And yeah nums length constraint is always at least 3 so yeah that should work 

        #Okay yeah I think thats close but you can also decrease the last elem instead 
        
        if len(nums)==3: 
            return 0 
        nums.sort()
        return min(nums[-1]-nums[2], nums[-3]-nums[0], nums[-2]-nums[1])
