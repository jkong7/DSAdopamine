class Solution(object):
    def maximumBeauty(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict 
        minn, maxx = min(nums)-k, max(nums)+k 
        prefix=[0]*(maxx-minn+2)
        for num in nums: 
            prefix[num-minn-k]+=1 
            prefix[num-minn+k+1]-=1
        roll, res = 0,0 
        for num in prefix: 
            roll+=num
            res=max(res, roll)
        return res 

        #Sweep line, just adjust index 0 to the needs of num-minn
        #start is -k (+=1) and end is +k+1 (-=1) and then just do the prefix sum 
        #finding the max sum 