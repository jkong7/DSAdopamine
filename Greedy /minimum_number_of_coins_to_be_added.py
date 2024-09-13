class Solution(object):
    def minimumAddedCoins(self, coins, target):
        """
        :type coins: List[int]
        :type target: int
        :rtype: int
        """
        coins.sort()
        total=0 
        count=0 

        for coin in coins: 
            while total+1<coin: 
                count+=1 
                total+=total+1
            total+=coin 
            if total>=target: 
                return count 
        while total<target: 
            total+=total+1 
            count+=1 
        return count 

        #And then otherwise IF the coin is valid (ie within total+1), we simply add 
        #coin to total and move on. After this, IF total is >=target we are good and
        #can return count 

        #BUT after iterating through coins we might still be short of target so we just
        #do one more round of total+=total+1 until total>=target. 

        #Note that no matter what on a coin iteration, we end up adding coin to total, 
        #its just that if it was invalid we have to do the nec total+1 adds before we 
        #can add coin 

        #This problem is a build upon of max num of consec values, that one simply 
        #required the is invalid? check (if total+1<coin means invalid otherwise total+=
        #coin)
