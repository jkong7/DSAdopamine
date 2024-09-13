class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        total=0 
        for coin in coins:
            if total+1<coin: 
                break
            total+=coin
        return total+1

        #If your total extended to one (next consec number which MUST BE avaliable) 
        #is LESS than the next smallest coin (sorted order), then the SMALLEST value 
        #we can make with that next coin is itself which is GREATER than the value
        #we NEED and thus right there, we cannot continue so we return total+1. 
        #total starts at 0 and we add coin everytime its valid, total+1 accomodates
        #for the empty 0 array thats always valid 

        #Greedy sort, if you get stopped by a num, there is no way anything further 
        #will be valid since even the MIN exceeds the limit