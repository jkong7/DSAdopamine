class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        #Monotonicity: If a sum n works, n+1 will also work
        #1. What is the search space? 
        #2. What is the condition that exhibits monotonicity? 
        #3. left will return minimum value that works 

        def condition(targetsum): 
            kcounter=1 
            summ=0 
            for num in nums: 
                summ+=num 
                if summ>targetsum: 
                    kcounter+=1 
                    summ=num 
                    if kcounter>k: 
                        return False
            return True 

        #mid is the sum, we are searching for mid in the SORTED space of 
        #possible sums 
        left, right=max(nums), sum(nums)
        while left<right: 
            mid=left+(right-left)//2
            if condition(mid): #answer exists at or to the left or mid
                right=mid
            else: 
                left=mid+1 #answer exists to the right of mid 
        return left 