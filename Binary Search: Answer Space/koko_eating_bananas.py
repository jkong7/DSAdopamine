class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        #Binary search template questions and set up for myself:
        #What is the monotinicity? A k rate that allows koko to eat all bananas k
        #means the k+1 rate also works 
        #1. What is the condition that has this monotinicity? k: true, k+1: true
        #2. What is the sorted search space that holds ALL possible k
        #Binary search will return minimum k such that condition is true
        #Condition: Koko is able to eat all bananas within h hours 

        import math 
        def condition(targetk): 
            hourcount=0 
            for pile in piles: 
                hourcount+=math.ceil(pile/float(targetk))
               #hourcount+=(pile-1)//targetk + 1   Same as ceil, tiny bit more optimal
            return hourcount<=h
        left, right=1,max(piles) #smallest pos k: 1, largest minimum k: max of piles
        while left<right: #going faster than that doesn't improve                  
            mid=left+(right-left)//2
            if condition(mid): #This works, everythng to the right works due to 
                right=mid       #monotonicity, thus minimum that works is
            else:               #this or to the left of this 
                left=mid+1
        return left    


        #Below was my condition function attempt 
        #Return true if targetk allows koko to finish all piles 
        #within h hours and false if not. I thought of subtract targetk
        #for iterations, below is technically correct but so ineff
        #b/c it uses differences (think small targetk large piles), 
        #time grows and grows          

        '''
        def condition(targetk): 
            hourcount=0
            pileindex=0 
            while pileindex<len(piles): 
                remaining=piles[pileindex]-targetk
                hourcount+=1 
                while remaining>=1: 
                    hourcount+=1 
                    remaining-=targetk
                pileindex+=1
            return True if hourcount<=h else False 
            '''
        #Whereas it's just using division for each pile to determine hourcount
        #for that pile-    ceil(pile/float(targetk)) which is O(1) 
        #and will never grow with larger piles/smaller targetk

        #Time complexity: condition is O(n) loop and then O(1) ceil so O(n)
        #binary search has O(log(max(piles))) time and for each binary search
        #iteration, the condition function is called once so overall: 
        #O(n log(max(piles)))

        #Note: 
        #1. log(n) portion is the halving/BinS. n IS SIZE OF SEARCH SPACE

        #2. Multiplied to this logn is the work done at each bin search iteration 
        #This is the time complexity of the condition function (or in simplest
        #bin search, nums[mid]==target is O(1)). Here its O(n)