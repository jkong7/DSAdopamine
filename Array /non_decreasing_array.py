class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Greedy in that the moment you get to a decrease, that HAS to be modified 

        #Case 1: Increase middle number i to exactly prev number and see if any 
        #following number is less than that target or there's another decrease 
        #(modify lesser up)

        flag, case1=False, None
        for i in range(1, len(nums)): 
            if flag: 
                if nums[i]<nums[i-1] or nums[i]<target:
                    case1=False
            else: 
                if nums[i]<nums[i-1]: 
                    target=nums[i-1]
                    flag=True 
        case1=True if case1==None else False

        #Case 2: Decrease prev(larger) to its prev value and see
        #if current is less than that modify or if there's another decrease 
        #(modify larger down)
        flag2, case2=False, None
        for i in range(1, len(nums)): 
            if flag2: 
                if nums[i]<nums[i-1]: 
                    case2=False #We can't handle two decreases
            else: 
                if nums[i]<nums[i-1]: 
                    flag2=True
                    target=nums[i-2]
                    if i-2<0: #No prev, doesn't have to modify to prev, so passes 
                        flag2=True 
                    elif nums[i-2]>nums[i]: 
                        case2=False 
                    elif nums[i-2]<=nums[i]: 
                        flag2=True #We've seen a decrease but it passed 
        case2=True if case2==None else False
        return case1 or case2
    
    

        #Two pass O(n), prob can make it into one pass but yeah its fine 

