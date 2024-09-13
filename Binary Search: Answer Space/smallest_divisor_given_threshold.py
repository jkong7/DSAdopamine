class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        import math 
        def condition(targetdivisor): 
            summ=0 
            for num in nums: 
                summ+=ceil(num/float(targetdivisor))
            return summ<=threshold
        left, right=1, max(nums)
        while left<right: 
            mid=left+(right-left)//2
            if condition(mid): 
                right=mid
            else: 
                left=mid+1

        #Monotonicity: A divisor of k that works will mean k+1 will also work 
        #Thus we use binary search 
        #Condition function: does targetidivisor stay within threshold? 
        #Search space: 1 to max(nums)