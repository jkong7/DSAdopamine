class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #Brainstorm 
        #Update min and max O(n) array scan

        #min so far, min will stay there if there isn't another number less than it 
        #until then, the max diff is used with the largest number found by the 
        #max pointer 

        #if max-min>0 and max-min>result: 
            #result=max-min 

        result=0 
        p_min=float('inf')
        for i in range(len(prices)):
            if prices[i]<p_min: 
                p_min=prices[i]
            if prices[i]-p_min>0 and prices[i]-p_min>result: 
                result=prices[i]-p_min 
        return result 

        #I was a little confused about my solution b/c I used i and j (even though
        #both served the exact same purpose and were incremented no matter what 
        #each time). I don't need one of the pointers (j) and instead p_min is the 
        #updated min and i iterates through the array, which serves purpose of 
        #finding a max for the min/difference AND potentially updating p_min 
        #Summary: 
        #1. p_min is stable and updates only when another min 
        #2. i finds diffs and potential p_min
        #3. result is potentailly updated at every instance of a diff

        #All max-min prices are considered (global) and min is constantly updated
        #(local)
