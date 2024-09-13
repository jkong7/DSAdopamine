class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Ah, nums length is 100 
        #Max num possible is max(nums)
        for num in range(0,101): 
            count=num 
            for x in nums: 
                if x>=num: 
                    count-=1 
            if count==0: 
                return num 
        return -1 


        