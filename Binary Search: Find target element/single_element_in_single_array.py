class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def condition(targetindex): 
            if targetindex%2==0: 
                return nums[targetindex]!=nums[targetindex+1]
            else: 
                return nums[targetindex]==nums[targetindex+1]
        left, right=0, len(nums)-1
        while left<right: 
            mid=left+(right-left)//2
            if condition(mid):
                right=mid
            else: 
                left=mid+1 
        return nums[left]

        #Again, just got to find the difference between the left and right side of
        #target, just got to think hard 
        #"Find the last/leftmost element where if index is even, number at index
        #and index+1 is different"
        #Monotonicity exists between the two sides of the single element with 
        #even/odd index number differences, so use condition to do our halves! 
        #HANDLES ALL EDGE CASES, as long as left and right cover ALL POSSIBLE INDEXES
        #i.e. left at very beg 0 and end at very end len(nums)-1 