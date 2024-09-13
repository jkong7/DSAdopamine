class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        #The max number is just buying all the cheapest ones first 
        costs.sort()
        count=0 
        for cost in costs: 
            coins-=cost 
            if coins>=0: 
                count+=1 
        return count 

        