class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #So think about it, the max sum will either be the LARGEST POSITIVE sum or 
        #the SMALLEST NEGATIVE sum, we basically want to consider the two extremes. 
        #So we can just do kadanes algorithm twice and then find the max between the two

        cur=0 
        maxx=0 
        for num in nums: 
            cur+=num
            if num>cur: 
                cur=num 
            maxx=max(maxx, cur)

        cur=0 
        minn=0 
        for num in nums: 
            cur+=num 
            if num<cur: 
                cur=num 
            minn=min(minn, cur)

        return max(maxx, -minn)

        #after revisiting kadanes, so dope, i bet kadanes pops
        #up a lot so its really good to know, its really intuitive to me though, its like
        #bottom up dp, at any step, do you just reset at the current num or go along 
        #with the entire path, which one is larger is the one you should take. 
        #For making as neg as possible, its just dont take current if the current num is 
        #smaller than it as thats the max at this step. 